/*=========================================================================

  Program:   Visualization Toolkit
  Module:    SpecularSpheres.cxx

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
//
// This examples demonstrates the effect of specular lighting.
//
#include "vtkSmartPointer.h"
#include "vtkSphereSource.h"
#include "vtkPolyDataMapper.h"
#include "vtkActor.h"
#include "vtkInteractorStyle.h"
#include "vtkObjectFactory.h"
#include "vtkRenderer.h"
#include "vtkRenderWindow.h"
#include "vtkRenderWindowInteractor.h"
#include "vtkProperty.h"
#include "vtkCamera.h"
#include "vtkLight.h"
#include "vtkOpenGLPolyDataMapper.h"
#include "vtkJPEGReader.h"
#include "vtkImageData.h"
#include <vtkPNGWriter.h>

#include <vtkPolyData.h>
#include <vtkPointData.h>
#include <vtkPolyDataReader.h>
#include <vtkPoints.h>
#include <vtkUnsignedCharArray.h>
#include <vtkFloatArray.h>
#include <vtkDoubleArray.h>
#include <vtkCellArray.h>
#include <vtkDataSetReader.h>
#include <vtkContourFilter.h>
#include <vtkRectilinearGrid.h>

#include <vtkCamera.h>
#include <vtkDataSetMapper.h>
#include <vtkRenderer.h>
#include <vtkActor.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkSmartPointer.h>
#include <math.h>

#include "TriangleList.h"
#include "tricase.cxx"



// ****************************************************************************
//  Function: GetNumberOfPoints
//
//  Arguments:
//     dims: an array of size 3 with the number of points in X, Y, and Z.
//           2D data sets would have Z=1
//
//  Returns:  the number of points in a rectilinear mesh
//
// ****************************************************************************

int GetNumberOfPoints(const int *dims)
{
    // 3D
    return dims[0]*dims[1]*dims[2];
    // 2D
    //return dims[0]*dims[1];
}

// ****************************************************************************
//  Function: GetNumberOfCells
//
//  Arguments:
//
//      dims: an array of size 3 with the number of points in X, Y, and Z.
//            2D data sets would have Z=1
//
//  Returns:  the number of cells in a rectilinear mesh
//
// ****************************************************************************

int GetNumberOfCells(const int *dims)
{
    // 3D
    return (dims[0]-1)*(dims[1]-1)*(dims[2]-1);
    // 2D
    //return (dims[0]-1)*(dims[1]-1);
}


// ****************************************************************************
//  Function: GetPointIndex
//
//  Arguments:
//      idx:  the logical index of a point.
//              0 <= idx[0] < dims[0]
//              1 <= idx[1] < dims[1]
//              2 <= idx[2] < dims[2] (or always 0 if 2D)
//      dims: an array of size 3 with the number of points in X, Y, and Z.
//            2D data sets would have Z=1
//
//  Returns:  the point index
//
// ****************************************************************************

int GetPointIndex(const int *idx, const int *dims)
{
    // 3D
    return idx[2]*dims[0]*dims[1]+idx[1]*dims[0]+idx[0];
    // 2D
    //return idx[1]*dims[0]+idx[0];
}


// ****************************************************************************
//  Function: GetCellIndex
//
//  Arguments:
//      idx:  the logical index of a cell.
//              0 <= idx[0] < dims[0]-1
//              1 <= idx[1] < dims[1]-1
//              2 <= idx[2] < dims[2]-1 (or always 0 if 2D)
//      dims: an array of size 3 with the number of points in X, Y, and Z.
//            2D data sets would have Z=1
//
//  Returns:  the cell index
//
// ****************************************************************************

int GetCellIndex(const int *idx, const int *dims)
{
    // 3D
    return idx[2]*(dims[0]-1)*(dims[1]-1)+idx[1]*(dims[0]-1)+idx[0];
    // 2D
    //return idx[1]*(dims[0]-1)+idx[0];
}

// ****************************************************************************
//  Function: GetLogicalPointIndex
//
//  Arguments:
//      idx (output):  the logical index of the point.
//              0 <= idx[0] < dims[0]
//              1 <= idx[1] < dims[1]
//              2 <= idx[2] < dims[2] (or always 0 if 2D)
//      pointId:  a number between 0 and (GetNumberOfPoints(dims)-1).
//      dims: an array of size 3 with the number of points in X, Y, and Z.
//            2D data sets would have Z=1
//
//  Returns:  None (argument idx is output)
//
// ****************************************************************************

void GetLogicalPointIndex(int *idx, int pointId, const int *dims)
{
    // 3D
     idx[0] = pointId%dims[0];
     idx[1] = (pointId/dims[0])%dims[1];
     idx[2] = pointId/(dims[0]*dims[1]);

    // 2D
    //idx[0] = pointId%dims[0];
    //idx[1] = pointId/dims[0];
}


// ****************************************************************************
//  Function: GetLogicalCellIndex
//
//  Arguments:
//      idx (output):  the logical index of the cell index.
//              0 <= idx[0] < dims[0]-1
//              1 <= idx[1] < dims[1]-1
//              2 <= idx[2] < dims[2]-1 (or always 0 if 2D)
//      cellId:  a number between 0 and (GetNumberOfCells(dims)-1).
//      dims: an array of size 3 with the number of points in X, Y, and Z.
//            2D data sets would have Z=1
//
//  Returns:  None (argument idx is output)
//
// ****************************************************************************

void GetLogicalCellIndex(int *idx, int cellId, const int *dims)
{
    // 3D
     idx[0] = cellId%(dims[0]-1);
     idx[1] = (cellId/(dims[0]-1))%(dims[1]-1);
     idx[2] = cellId/((dims[0]-1)*(dims[1]-1));

    // 2D
    //idx[0] = cellId%(dims[0]-1);
    //idx[1] = cellId/(dims[0]-1);
}

//My helper function to find the case
int IdentifyCase(int* values, float* F){
  int icase = 0;
  for(int i = 0; i < 8; i++){
    if(F[values[i]] > 3.2){
        icase += pow(2, i);
    }
  }
  return icase;
}


int main()
{
    int  i, j;

    vtkDataSetReader *rdr = vtkDataSetReader::New();
    rdr->SetFileName("proj6B.vtk");
    rdr->Update();

    int dims[3];
    vtkRectilinearGrid *rgrid = (vtkRectilinearGrid *) rdr->GetOutput();
    rgrid->GetDimensions(dims);

    float *X = (float *) rgrid->GetXCoordinates()->GetVoidPointer(0);
    float *Y = (float *) rgrid->GetYCoordinates()->GetVoidPointer(0);
    float *Z = (float *) rgrid->GetZCoordinates()->GetVoidPointer(0);
    float *F = (float *) rgrid->GetPointData()->GetScalars()->GetVoidPointer(0);

    // Add 4 segments that put a frame around your isolines.  This also
    // documents how to use "AddSegment".
    TriangleList sl;



// YOUR CODE TO GENERATE ISOLINES SHOULD GO HERE!


    int icase,segs,k= 0;
    int cellidxout[3];
    int lowerleft[2];
    int lowerright[2];
    int upperleft[2];
    int upperright[2];
    int values[8];
    int edge1,edge2, edge3 = 0;;
    float pt1[3], pt2[3], pt3[3];
    static int edges[12][2] = {{0,1},{1,3},{2,3},{0,2},{4,5},{5,7},{6,7},{4,6},{0,4},{1,5},{2,6},{3,7}};

    cellidxout[0] = 0;
    cellidxout[1] = 0;
    cellidxout[2] = 0;


    pt1[0] = 0.0;
    pt1[1] = 0.0;
    pt1[2] = 0.0;
    pt2[0] = 0.0;
    pt2[1] = 0.0;
    pt2[2] = 0.0;
    pt3[0] = 0.0;
    pt3[1] = 0.0;
    pt3[2] = 0.0;


    values[0] = 0;
    values[1] = 0;
    values[2] = 0;
    values[3] = 0;
    values[4] = 0;
    values[5] = 0;
    values[6] = 0;
    values[7] = 0;


    int A = 0;
    int B = 0;
    int C = 0;
    int lX = 0;
    int lY = 0;
    int uX = 0;
    int uY = 0;
    int lZ = 0;
    int uZ = 0;
    int s = 0;
    int vertices[8][3];

    for(k = 0; k < GetNumberOfCells(dims); k++){
       GetLogicalCellIndex(cellidxout,k,dims);
       pt1[0] = 0.0;
       pt1[1] = 0.0;
       pt1[2] = 0.0;
       pt2[0] = 0.0;
       pt2[1] = 0.0;
       pt2[2] = 0.0;
       pt3[0] = 0.0;
       pt3[1] = 0.0;
       pt3[2] = 0.0;
       values[0] = 0;
       values[1] = 0;
       values[2] = 0;
       values[3] = 0;
       values[4] = 0;
       values[5] = 0;
       values[6] = 0;
       values[7] = 0;

       vertices[0][0] = cellidxout[0];
       vertices[0][1] = cellidxout[1];
       vertices[0][2] = cellidxout[2];
       vertices[1][0] = cellidxout[0]+1;
       vertices[1][1] = cellidxout[1];
       vertices[1][2] = cellidxout[2];
       vertices[2][0] = cellidxout[0];
       vertices[2][1] = cellidxout[1]+1;
       vertices[2][2] = cellidxout[2];
       vertices[3][0] = cellidxout[0]+1;
       vertices[3][1] = cellidxout[1]+1;
       vertices[3][2] = cellidxout[2];
       vertices[4][0] = cellidxout[0];
       vertices[4][1] = cellidxout[1];
       vertices[4][2] = cellidxout[2]+1;
       vertices[5][0] = cellidxout[0]+1;
       vertices[5][1] = cellidxout[1];
       vertices[5][2] = cellidxout[2]+1;
       vertices[6][0] = cellidxout[0];
       vertices[6][1] = cellidxout[1]+1;
       vertices[6][2] = cellidxout[2]+1;
       vertices[7][0] = cellidxout[0]+1;
       vertices[7][1] = cellidxout[1]+1;
       vertices[7][2] = cellidxout[2]+1;



       for(int x = 0; x < 8; x++){
         values[x] = GetPointIndex(vertices[x], dims);
       }

       icase = IdentifyCase(values, F);


       s = 0;
       while(triCase[icase][3*s] != -1){
         edge1 = triCase[icase][3*s];
         A = values[edges[edge1][0]];
         B = values[edges[edge1][1]];
         lX = vertices[edges[edge1][0]][0];
         uX = vertices[edges[edge1][1]][0];
         lY = vertices[edges[edge1][0]][1];
         uY = vertices[edges[edge1][1]][1];
         lZ = vertices[edges[edge1][0]][2];
         uZ = vertices[edges[edge1][1]][2];

        pt1[0] = X[lX] + ((3.2 - F[A])/(F[B] - F[A]))*(X[uX] - X[lX]);
        pt1[1] = Y[lY] + ((3.2 - F[A])/(F[B] - F[A]))*(Y[uY] - Y[lY]);
        pt1[2] = Z[lZ] + ((3.2 - F[A])/(F[B] - F[A]))*(Z[uZ] - Z[lZ]);

        edge2 = triCase[icase][3*s + 1];
        A = values[edges[edge2][0]];
        B = values[edges[edge2][1]];
        lX = vertices[edges[edge2][0]][0];
        uX = vertices[edges[edge2][1]][0];
        lY = vertices[edges[edge2][0]][1];
        uY = vertices[edges[edge2][1]][1];
        lZ = vertices[edges[edge2][0]][2];
        uZ = vertices[edges[edge2][1]][2];

        pt2[0] = X[lX] + ((3.2 - F[A])/(F[B] - F[A]))*(X[uX] - X[lX]);
        pt2[1] = Y[lY] + ((3.2 - F[A])/(F[B] - F[A]))*(Y[uY] - Y[lY]);
        pt2[2] = Z[lZ] + ((3.2 - F[A])/(F[B] - F[A]))*(Z[uZ] - Z[lZ]);


        edge3 = triCase[icase][3*s + 2];
        A = values[edges[edge3][0]];
        B = values[edges[edge3][1]];
        lX = vertices[edges[edge3][0]][0];
        uX = vertices[edges[edge3][1]][0];
        lY = vertices[edges[edge3][0]][1];
        uY = vertices[edges[edge3][1]][1];
        lZ = vertices[edges[edge3][0]][2];
        uZ = vertices[edges[edge3][1]][2];

        pt3[0] = X[lX] + ((3.2 - F[A])/(F[B] - F[A]))*(X[uX] - X[lX]);
        pt3[1] = Y[lY] + ((3.2 - F[A])/(F[B] - F[A]))*(Y[uY] - Y[lY]);
        pt3[2] = Z[lZ] + ((3.2 - F[A])/(F[B] - F[A]))*(Z[uZ] - Z[lZ]);
        s += 1;

        sl.AddTriangle(pt1[0], pt1[1],pt1[2], pt2[0], pt2[1],pt2[2],pt3[0],pt3[1],pt3[2]);

       }

     }

//end of my code





    vtkPolyData *pd = sl.MakePolyData();

    //This can be useful for debugging
/*
    vtkDataSetWriter *writer = vtkDataSetWriter::New();
    writer->SetFileName("paths.vtk");
    writer->SetInputData(pd);
    writer->Write();
 */

    vtkSmartPointer<vtkDataSetMapper> win1Mapper =
      vtkSmartPointer<vtkDataSetMapper>::New();
    win1Mapper->SetInputData(pd);
    win1Mapper->SetScalarRange(0, 0.15);

    vtkSmartPointer<vtkActor> win1Actor =
      vtkSmartPointer<vtkActor>::New();
    win1Actor->SetMapper(win1Mapper);

    vtkSmartPointer<vtkRenderer> ren1 =
      vtkSmartPointer<vtkRenderer>::New();

    vtkSmartPointer<vtkRenderWindow> renWin =
      vtkSmartPointer<vtkRenderWindow>::New();
    renWin->AddRenderer(ren1);

    vtkSmartPointer<vtkRenderWindowInteractor> iren =
      vtkSmartPointer<vtkRenderWindowInteractor>::New();
    iren->SetRenderWindow(renWin);
    ren1->AddActor(win1Actor);
    ren1->SetBackground(0.0, 0.0, 0.0);
    renWin->SetSize(800, 800);

    ren1->GetActiveCamera()->SetFocalPoint(0,0,0);
    ren1->GetActiveCamera()->SetPosition(0,0,50);
    ren1->GetActiveCamera()->SetViewUp(0,1,0);
    ren1->GetActiveCamera()->SetClippingRange(20, 120);
    ren1->GetActiveCamera()->SetDistance(30);

    // This starts the event loop and invokes an initial render.
    //
    iren->Initialize();
    iren->Start();

    pd->Delete();
}
