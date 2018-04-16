
#include "vtkSmartPointer.h"
#include "vtkPolyDataMapper.h"
#include "vtkActor.h"
#include "vtkObjectFactory.h"
#include "vtkRenderer.h"
#include "vtkRenderWindow.h"
#include "vtkRenderWindowInteractor.h"
#include "vtkProperty.h"

#include <vtkPolyData.h>
#include <vtkPointData.h>
#include <vtkPolyDataReader.h>
#include <vtkPolyDataMapper.h>
#include <vtkPoints.h>
#include <vtkDataSetReader.h>
#include <vtkContourFilter.h>
#include <vtkRectilinearGrid.h>

#include <vtkDataSetMapper.h>
#include <vtkRenderer.h>
#include <vtkActor.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkSmartPointer.h>

#include <vtkPlane.h>
#include <vtkStructuredGrid.h>
#include <vtkHedgehog.h>

#include <vtkStreamTracer.h>
#include <vtkCutter.h>
#include <vtkMaskPoints.h>
#include <vtkLineSource.h>


int main()
{
    vtkDataSetReader *rdr = vtkDataSetReader::New();
    rdr->SetFileName("proj8.vtk");
    rdr->Update();

    vtkSmartPointer<vtkRenderWindow> renWin =
     vtkSmartPointer<vtkRenderWindow>::New();

//Isosurfaces
    vtkContourFilter *isosurface1 = vtkContourFilter::New();
    isosurface1->SetNumberOfContours(1);
    isosurface1->SetValue(0,2.5);
    isosurface1->SetInputConnection(rdr->GetOutputPort());

    vtkSmartPointer<vtkPolyDataMapper> isoR1 = vtkSmartPointer<vtkPolyDataMapper>::New();
    isoR1->SetInputConnection(isosurface1->GetOutputPort());


    vtkContourFilter *isosurface2 = vtkContourFilter::New();
    isosurface2->SetNumberOfContours(1);
    isosurface2->SetValue(0,5.0);
    isosurface2->SetInputConnection(rdr->GetOutputPort());


    vtkSmartPointer<vtkPolyDataMapper> isoR2 = vtkSmartPointer<vtkPolyDataMapper>::New();
    isoR2->SetInputConnection(isosurface2->GetOutputPort());

    vtkSmartPointer<vtkActor> win1Actor =
      vtkSmartPointer<vtkActor>::New();
    win1Actor->SetMapper(isoR1);
    win1Actor->GetMapper()->ScalarVisibilityOff();
    win1Actor->GetProperty()->SetColor(0.0,1.0,0.0);

    vtkSmartPointer<vtkActor> win2Actor =
      vtkSmartPointer<vtkActor>::New();
    win2Actor->SetMapper(isoR2);
    win2Actor->GetMapper()->ScalarVisibilityOff();
    win2Actor->GetProperty()->SetColor(0.0,0.0,1.0);



//Color Mapping
  rdr->GetOutput()->GetPointData()->SetActiveAttribute("hardyglobal",vtkDataSetAttributes::SCALARS);

  vtkSmartPointer<vtkPlane> plane1 = vtkSmartPointer<vtkPlane>::New();
  plane1->SetOrigin(rdr->GetOutput()->GetCenter());
  plane1->SetNormal(0,1,0.5);


  vtkSmartPointer<vtkPlane> plane2 = vtkSmartPointer<vtkPlane>::New();
  plane2->SetOrigin(rdr->GetOutput()->GetCenter());
  plane2->SetNormal(1.0,1.0,1.0);


  vtkSmartPointer<vtkCutter> cutter = vtkSmartPointer<vtkCutter>::New();
  cutter->SetCutFunction(plane1);
  cutter->SetInputConnection(rdr->GetOutputPort());
  cutter->Update();

  vtkSmartPointer<vtkCutter> cutter2 = vtkSmartPointer<vtkCutter>::New();
  cutter2->SetCutFunction(plane2);
  cutter2->SetInputConnection(rdr->GetOutputPort());
  cutter2->Update();


  vtkSmartPointer<vtkDataSetMapper> colorMapper = vtkSmartPointer<vtkDataSetMapper>::New();
  colorMapper->SetInputConnection(cutter->GetOutputPort());
  colorMapper->SetScalarRange(2,5);

  vtkSmartPointer<vtkDataSetMapper> colorMapper2 = vtkSmartPointer<vtkDataSetMapper>::New();
  colorMapper2->SetInputConnection(cutter2->GetOutputPort());
  colorMapper2->SetScalarRange(2,5);



  vtkSmartPointer<vtkActor> colorActor = vtkSmartPointer<vtkActor>::New();
  colorActor->SetMapper(colorMapper);

  vtkSmartPointer<vtkActor> colorActor2 = vtkSmartPointer<vtkActor>::New();
  colorActor2->SetMapper(colorMapper2);


//Hedgehog
    rdr->GetOutput()->GetPointData()->SetActiveAttribute("grad",1);

    vtkSmartPointer<vtkMaskPoints> hedgeMask = vtkSmartPointer<vtkMaskPoints>::New();
    hedgeMask->SetOnRatio(69);
    hedgeMask->SetInputConnection(rdr->GetOutputPort());
    hedgeMask->Update();

    vtkSmartPointer<vtkHedgeHog> hedgehog = vtkSmartPointer<vtkHedgeHog>::New();
    hedgehog->SetInputConnection(hedgeMask->GetOutputPort());
    hedgehog->Update();

    vtkSmartPointer<vtkPolyDataMapper> hedgehogMap = vtkSmartPointer<vtkPolyDataMapper>::New();
    hedgehogMap->SetInputConnection(hedgehog->GetOutputPort());
    hedgehogMap->SetScalarRange(2,5);


    vtkSmartPointer<vtkActor> hedgehogActor = vtkSmartPointer<vtkActor>
    ::New();
    hedgehogActor->SetMapper(hedgehogMap);


    vtkSmartPointer<vtkPolyDataMapper> hedgehogMapMask = vtkSmartPointer<vtkPolyDataMapper>::New();
    hedgehogMapMask->SetInputConnection(hedgeMask->GetOutputPort());
    hedgehogMapMask->SetScalarRange(rdr->GetOutput()->GetScalarRange());

    vtkSmartPointer<vtkActor> maskActor = vtkSmartPointer<vtkActor>::New();
    maskActor->SetMapper(hedgehogMapMask);


//Isolines/Streamlines

    rdr->GetOutput()->GetPointData()->SetActiveAttribute("grad",vtkDataSetAttributes::VECTORS);
    rdr->GetOutput()->GetPointData()->SetActiveAttribute("hardyglobal",0);


   vtkSmartPointer<vtkLineSource> seed = vtkSmartPointer<vtkLineSource>::New();
   seed->SetPoint1(-9,0,0);
   seed->SetPoint2(9,0,0);
   seed->SetResolution(19);

      vtkSmartPointer<vtkStreamTracer> isoline = vtkSmartPointer<vtkStreamTracer>::New();
      isoline->SetIntegratorTypeToRungeKutta4();
      isoline->SetMaximumPropagation(100);
      //isoline->SetIntegratorType(1);
      isoline->SetInputConnection(rdr->GetOutputPort());
      isoline->SetSourceConnection(seed->GetOutputPort());
      vtkSmartPointer<vtkPolyDataMapper> isoMap = vtkSmartPointer<vtkPolyDataMapper>::New();
      isoMap->SetInputConnection(isoline->GetOutputPort());
      isoMap->SetScalarRange(2,5);
      isoMap->Update();
      vtkSmartPointer<vtkActor> isoActor = vtkSmartPointer<vtkActor>::New();
      isoActor->SetMapper(isoMap);
      isoActor->VisibilityOn();






//Renderers
    vtkSmartPointer<vtkRenderer> ren1 =
      vtkSmartPointer<vtkRenderer>::New();

    renWin->AddRenderer(ren1);

    vtkSmartPointer<vtkRenderWindowInteractor> iren =
      vtkSmartPointer<vtkRenderWindowInteractor>::New();

//Renderer for ColorMap
      vtkSmartPointer<vtkRenderer> ren2 =
        vtkSmartPointer<vtkRenderer>::New();

      renWin->AddRenderer(ren2);

//Renderer for Hedgehog
      vtkSmartPointer<vtkRenderer> ren3 =
        vtkSmartPointer<vtkRenderer>::New();

    renWin->AddRenderer(ren3);

//Renderer for Streamlines
    vtkSmartPointer<vtkRenderer> ren4 =
      vtkSmartPointer<vtkRenderer>::New();

  renWin->AddRenderer(ren4);


    iren->SetRenderWindow(renWin);

//Add isosurface
    renWin->AddRenderer(ren1);
    ren1->SetViewport(0,0,0.5,0.5);

//Add Isolines

    renWin->AddRenderer(ren4);
    ren4->SetViewport(0.5,0.5,1.0,1.0);

//ColorMap
    renWin->AddRenderer(ren2);
    ren2->SetViewport(0,0.5,0.5,1.0);

//Hedgehog
    renWin->AddRenderer(ren3);
    ren3->SetViewport(0.5,0,1.0,0.5);




//Add actors
    ren1->AddActor(win1Actor);
    ren1->AddActor(win2Actor);
    ren2->AddActor(colorActor);
    ren2->AddActor(colorActor2);
    ren3->AddActor(hedgehogActor);
    ren3->AddActor(maskActor);
    ren4->AddActor(isoActor);


    ren1->SetBackground(0.0, 0.0, 0.0);
    ren2->SetBackground(0.0, 0.0, 0.0);
    ren3->SetBackground(0.0, 0.0, 0.0);
    ren4->SetBackground(0.0, 0.0, 0.0);

    renWin->SetSize(800, 800);


    iren->Initialize();
    iren->Start();


}
