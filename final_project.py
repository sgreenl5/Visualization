#Sarah Greenlaw Final Project

frame_idx=0

def PauseFewSeconds():
  global frame_idx
  for i in range(50):
    sw.fileName="frames/m%02d" %(frame_idx)
    frame_idx = frame_idx + 1
    SetSaveWindowAttributes(sw)
    MySaveWindow()

def Pause():
  global frame_idx
  for i in range(5):
    sw.fileName="frames/m%02d" %(frame_idx)
    frame_idx = frame_idx + 1
    SetSaveWindowAttributes(sw)
    MySaveWindow()

def Slow():
  global frame_idx
  sw.fileName="frames/m%02d" %(frame_idx)
  frame_idx = frame_idx + 1
  SetSaveWindowAttributes(sw)
  MySaveWindow()
  sw.fileName="frames/m%02d" %(frame_idx)
  frame_idx = frame_idx+1
  SetSaveWindowAttributes(sw)
  MySaveWindow()

actually_do_a_save=1
def MySaveWindow():
  global actually_do_a_save
  if (actually_do_a_save):
     SaveWindow()


sw = SaveWindowAttributes()
sw.family = 0
sw.width = 800
sw.height = 800
sw.format = sw.PPM
LEN = 160


RestoreSession("/Users/sarahgreenlaw/Documents/CIS410/contour.session", 0)


SetSaveWindowAttributes(sw)
MySaveWindow()

ToggleSpinMode()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.462428, 0.155511, 0.872913)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0257851, 0.986441, -0.162076)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()


# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.592617, 0.159415, 0.789552)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0398987, 0.984826, -0.168895)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.708494, 0.16077, 0.68716)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0549082, 0.983312, -0.173445)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = +1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.807281, 0.159544, 0.568193)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0704538, 0.981934, -0.175619)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.886608, 0.155767, 0.435504)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0861626, 0.980726, -0.175365)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.944572, 0.149528, 0.292275)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.101658, 0.979717, -0.172687)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.979785, 0.140978, 0.14194)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.116568, 0.978931, -0.167651)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.9914, 0.130322, -0.0118941)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.130535, 0.978386, -0.160378)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.979141, 0.117815, -0.165539)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.143225, 0.978097, -0.151041)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.9433, 0.103757, -0.31531)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.154333, 0.978069, -0.139865)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.884737, 0.0884851, -0.457614)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.163592, 0.978304, -0.127117)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.804857, 0.0723659, -0.58904)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.170781, 0.978796, -0.113104)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.705575, 0.0557857, -0.706436)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.175727, 0.979533, -0.0981613)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.589273, 0.0391423, -0.806985)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.178312, 0.980497, -0.0826474)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.458739, 0.0228347, -0.888278)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.178473, 0.981666, -0.0669344)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.317104, 0.007254, -0.948363)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.176206, 0.98301, -0.0513992)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.167765, -0.00722608, -0.985801)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.171567, 0.984499, -0.0364141)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0143029, -0.0202583, -0.999692)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.164666, 0.986096, -0.0223387)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.139602, -0.0315302, -0.989706)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.155669, 0.987763, -0.00951052)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.290258, -0.0407713, -0.956079)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.144792, 0.989461, 0.00176286)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.434053, -0.0477601, -0.89962)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.132295, 0.991147, 0.011211)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.567538, -0.052329, -0.821683)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.118478, 0.992782, 0.0186075)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.687512, -0.0543684, -0.724135)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.103672, 0.994327, 0.0237747)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.791098, -0.0538293, -0.609317)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0882335, 0.995745, 0.0265889)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.875811, -0.0507248, -0.479982)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0725314, 0.997001, 0.0269825)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.93962, -0.0451292, -0.339232)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0569427, 0.998066, 0.0249461)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.980994, -0.0371768, -0.190442)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0418412, 0.998913, 0.0205285)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.998942, -0.0270583, -0.0371813)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.027589, 0.999524, 0.0138357)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.993033, -0.0150163, 0.116876)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.0145281, 0.999882, 0.00502821)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.963409, -0.00133964, 0.268034)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (0.00297153, 0.999979, -0.00568281)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.910779, 0.0136437, 0.412668)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.00680346, 0.999814, -0.0180405)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.836407, 0.0295744, 0.54731)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0145625, 0.99939, -0.0317484)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.742076, 0.0460704, 0.668731)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0201194, 0.998717, -0.0464778)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.630048, 0.0627361, 0.774018)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0233411, 0.997811, -0.0618755)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.50301, 0.0791718, 0.860647)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0241501, 0.996694, -0.0775723)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.364008, 0.0949834, 0.92654)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0225272, 0.995393, -0.0931916)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.216376, 0.109792, 0.970117)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0185112, 0.993939, -0.108359)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0636542, 0.123241, 0.990333)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0121984, 0.992368, -0.12271)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0904944, 0.13501, 0.986703)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.00374029, 0.990715, -0.135902)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
Slow()


ToggleSpinMode()
i = 0
while i <= LEN:
 SetTimeSliderState(i)
 sw.fileName="frames/m%02d" %(frame_idx)
 frame_idx = frame_idx+1
 SetSaveWindowAttributes(sw)
 MySaveWindow()
 Slow()
 i += 1


# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0274171, 0.0528848, 0.998224)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.00186056, 0.998595, -0.0529555)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

ToggleSpinMode()
# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0230041, 0.043885, 0.998772)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0092154, 0.999003, -0.0436829)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0269356, 0.0431853, 0.998704)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.00976321, 0.99903, -0.0429361)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.030867, 0.0424872, 0.99862)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0103081, 0.999057, -0.0421871)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0347983, 0.0417906, 0.99852)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.01085, 0.999082, -0.041436)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0387295, 0.0410956, 0.998404)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0113889, 0.999107, -0.0406827)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0426604, 0.0404022, 0.998272)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0119249, 0.999131, -0.0399273)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0465911, 0.0397103, 0.998124)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0124579, 0.999155, -0.0391698)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0505214, 0.03902, 0.99796)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0129879, 0.999178, -0.0384101)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0544512, 0.0383314, 0.99778)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0135149, 0.9992, -0.0376483)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0583806, 0.0376443, 0.997584)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0140389, 0.999221, -0.0368845)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0623095, 0.0369589, 0.997372)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0145599, 0.999241, -0.0361185)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0662377, 0.0362751, 0.997144)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0150778, 0.999261, -0.0353505)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0701652, 0.0355929, 0.9969)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0155928, 0.99928, -0.0345805)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.074092, 0.0349125, 0.99664)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0161046, 0.999299, -0.0338083)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.078018, 0.0342337, 0.996364)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0166135, 0.999316, -0.0330342)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0819432, 0.0335565, 0.996072)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0171192, 0.999333, -0.032258)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0858674, 0.0328811, 0.995764)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.017622, 0.999349, -0.0314799)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0897906, 0.0322074, 0.99544)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0181216, 0.999364, -0.0306997)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0937127, 0.0315353, 0.9951)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0186181, 0.999379, -0.0299176)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0976338, 0.030865, 0.994744)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0191116, 0.999393, -0.0291335)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.101554, 0.0301965, 0.994372)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.019602, 0.999406, -0.0283474)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.105472, 0.0295297, 0.993984)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0200892, 0.999418, -0.0275594)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.109389, 0.0288646, 0.99358)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0205734, 0.99943, -0.0267695)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.113305, 0.0282013, 0.99316)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0210544, 0.999441, -0.0259777)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.11722, 0.0275398, 0.992724)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0215323, 0.999451, -0.0251839)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.121133, 0.0268801, 0.992272)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.022007, 0.99946, -0.0243883)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.125044, 0.0262222, 0.991805)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0224787, 0.999469, -0.0235908)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.128954, 0.0255661, 0.991321)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0229471, 0.999477, -0.0227914)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.132862, 0.0249118, 0.990821)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0234124, 0.999484, -0.0219902)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.136768, 0.0242594, 0.990306)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0238745, 0.99949, -0.0211871)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.140673, 0.0236088, 0.989775)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0243335, 0.999496, -0.0203823)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.144575, 0.0229601, 0.989227)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0247893, 0.999501, -0.0195756)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.148476, 0.0223132, 0.988664)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0252418, 0.999505, -0.0187671)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.152375, 0.0216682, 0.988085)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0256912, 0.999509, -0.0179568)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.156271, 0.021025, 0.98749)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0261374, 0.999511, -0.0171447)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.160166, 0.0203838, 0.98688)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0265804, 0.999513, -0.0163309)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.164058, 0.0197445, 0.986253)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0270201, 0.999514, -0.0155154)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.167948, 0.0191071, 0.985611)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0274566, 0.999515, -0.0146981)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.171835, 0.0184716, 0.984953)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0278899, 0.999515, -0.0138791)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.175721, 0.0178381, 0.984278)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0283199, 0.999514, -0.0130583)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.179603, 0.0172065, 0.983589)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0287467, 0.999512, -0.0122359)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.183483, 0.0165769, 0.982883)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0291703, 0.999509, -0.0114118)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.187361, 0.0159492, 0.982162)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0295905, 0.999506, -0.0105861)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.191236, 0.0153236, 0.981424)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0300076, 0.999502, -0.00975868)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.195108, 0.0146999, 0.980672)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0304213, 0.999497, -0.00892964)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.198978, 0.0140782, 0.979903)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0308317, 0.999492, -0.00809897)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.202845, 0.0134585, 0.979118)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0312389, 0.999486, -0.00726669)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.206708, 0.0128409, 0.978318)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0316428, 0.999479, -0.00643281)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.210569, 0.0122252, 0.977503)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0320433, 0.999471, -0.00559734)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.214427, 0.0116116, 0.976671)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0324406, 0.999462, -0.00476031)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.218282, 0.0110001, 0.975824)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0328345, 0.999453, -0.00392172)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.222133, 0.0103906, 0.974961)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0332251, 0.999443, -0.00308158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.225982, 0.0097832, 0.974082)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0336124, 0.999432, -0.00223991)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.229827, 0.00917787, 0.973188)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0339964, 0.999421, -0.00139673)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.233668, 0.00857463, 0.972279)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.034377, 0.999409, -0.000552043)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.237507, 0.00797348, 0.971353)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0347543, 0.999396, 0.000294132)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.241342, 0.00737445, 0.970412)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0351282, 0.999382, 0.00114178)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.245173, 0.00677753, 0.969456)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0354987, 0.999368, 0.00199089)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.249001, 0.00618275, 0.968484)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0358659, 0.999353, 0.00284145)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.252825, 0.0055901, 0.967496)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0362298, 0.999337, 0.00369345)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.256645, 0.00499959, 0.966493)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0365902, 0.99932, 0.00454686)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.260462, 0.00441125, 0.965474)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0369473, 0.999303, 0.00540168)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.264275, 0.00382507, 0.96444)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0373009, 0.999284, 0.00625789)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.268084, 0.00324107, 0.96339)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0376512, 0.999266, 0.00711548)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.271889, 0.00265925, 0.962325)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0379981, 0.999246, 0.00797443)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.275689, 0.00207963, 0.961245)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0383416, 0.999226, 0.00883474)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.279486, 0.00150222, 0.960149)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0386816, 0.999205, 0.00969638)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.283279, 0.000927017, 0.959037)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0390183, 0.999183, 0.0105593)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.287067, 0.000354039, 0.95791)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0393515, 0.99916, 0.0114236)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.290852, -0.000216706, 0.956768)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0396813, 0.999137, 0.0122892)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.294632, -0.000785209, 0.955611)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0400077, 0.999113, 0.013156)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.298407, -0.00135146, 0.954438)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0403306, 0.999088, 0.0140241)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.302178, -0.00191545, 0.95325)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0406501, 0.999062, 0.0148935)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.305945, -0.00247717, 0.952046)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0409661, 0.999036, 0.0157641)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.309707, -0.00303662, 0.950827)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0412787, 0.999009, 0.0166359)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.313464, -0.00359377, 0.949593)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0415878, 0.998981, 0.0175089)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.317216, -0.00414863, 0.948344)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0418935, 0.998953, 0.0183832)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.320964, -0.00470118, 0.94708)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0421956, 0.998924, 0.0192586)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.324707, -0.00525141, 0.9458)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0424944, 0.998894, 0.0201352)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.328445, -0.00579933, 0.944505)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0427896, 0.998863, 0.0210129)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.332179, -0.00634491, 0.943195)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0430813, 0.998832, 0.0218918)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.335907, -0.00688814, 0.94187)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0433696, 0.9988, 0.0227717)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.33963, -0.00742903, 0.94053)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0436544, 0.998767, 0.0236528)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.343348, -0.00796756, 0.939174)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0439356, 0.998733, 0.024535)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.347061, -0.00850372, 0.937804)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0442134, 0.998699, 0.0254183)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.350768, -0.0090375, 0.936419)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0444877, 0.998664, 0.0263027)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.354471, -0.00956889, 0.935018)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0447584, 0.998628, 0.027188)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.358168, -0.0100979, 0.933603)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0450257, 0.998591, 0.0280745)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.361859, -0.0106245, 0.932172)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0452894, 0.998554, 0.0289619)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.365545, -0.0111487, 0.930727)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0455496, 0.998516, 0.0298504)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.369226, -0.0116705, 0.929267)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0458062, 0.998477, 0.0307399)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.3729, -0.0121898, 0.927791)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0460594, 0.998438, 0.0316303)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.37657, -0.0127067, 0.926301)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.046309, 0.998398, 0.0325217)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.380233, -0.0132211, 0.924796)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.046555, 0.998357, 0.033414)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.383891, -0.0137332, 0.923276)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0467975, 0.998315, 0.0343073)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.387542, -0.0142427, 0.921742)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0470365, 0.998273, 0.0352015)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.391188, -0.0147498, 0.920192)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0472719, 0.99823, 0.0360967)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.394828, -0.0152544, 0.918628)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0475038, 0.998186, 0.0369927)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.398462, -0.0157565, 0.917049)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0477321, 0.998141, 0.0378896)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.40209, -0.0162561, 0.915456)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0479568, 0.998096, 0.0387873)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.405712, -0.0167532, 0.913847)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0481779, 0.99805, 0.0396859)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.409327, -0.0172478, 0.912225)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0483955, 0.998003, 0.0405854)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.412937, -0.0177399, 0.910587)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0486096, 0.997956, 0.0414856)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.41654, -0.0182294, 0.908935)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.04882, 0.997908, 0.0423867)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.420136, -0.0187164, 0.907268)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0490268, 0.997859, 0.0432885)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.423726, -0.0192009, 0.905587)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0492301, 0.997809, 0.0441912)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.42731, -0.0196828, 0.903891)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0494298, 0.997759, 0.0450945)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.430887, -0.0201622, 0.902181)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0496259, 0.997708, 0.0459987)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.434458, -0.020639, 0.900456)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0498184, 0.997656, 0.0469035)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.438021, -0.0211132, 0.898717)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0500073, 0.997604, 0.0478091)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.441578, -0.0215848, 0.896963)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0501926, 0.997551, 0.0487154)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.445129, -0.0220539, 0.895195)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0503743, 0.997497, 0.0496224)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.448672, -0.0225203, 0.893413)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0505524, 0.997442, 0.05053)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.452209, -0.0229842, 0.891616)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0507268, 0.997387, 0.0514383)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.455738, -0.0234454, 0.889805)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0508977, 0.997331, 0.0523473)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.459261, -0.023904, 0.88798)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0510649, 0.997274, 0.0532568)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.462776, -0.02436, 0.88614)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0512286, 0.997217, 0.054167)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.466285, -0.0248134, 0.884287)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0513886, 0.997159, 0.0550778)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.469786, -0.0252641, 0.882419)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.051545, 0.9971, 0.0559892)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.47328, -0.0257121, 0.880537)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0516977, 0.99704, 0.0569011)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.476767, -0.0261575, 0.878641)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0518469, 0.99698, 0.0578136)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.480246, -0.0266003, 0.87673)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0519924, 0.996919, 0.0587266)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.483718, -0.0270403, 0.874806)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0521342, 0.996858, 0.0596402)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.487182, -0.0274777, 0.872868)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0522725, 0.996795, 0.0605543)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.490639, -0.0279124, 0.870916)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0524071, 0.996732, 0.0614688)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.494089, -0.0283444, 0.868949)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.052538, 0.996668, 0.0623839)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.49753, -0.0287737, 0.866969)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0526653, 0.996604, 0.0632994)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.500964, -0.0292003, 0.864975)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.052789, 0.996539, 0.0642153)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.504391, -0.0296242, 0.862967)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.052909, 0.996473, 0.0651317)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.507809, -0.0300454, 0.860946)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0530254, 0.996406, 0.0660485)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.51122, -0.0304638, 0.85891)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0531381, 0.996339, 0.0669657)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.514622, -0.0308795, 0.856861)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0532472, 0.996271, 0.0678834)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.518017, -0.0312925, 0.854798)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0533526, 0.996203, 0.0688013)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.521404, -0.0317027, 0.852721)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0534544, 0.996133, 0.0697197)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.524782, -0.0321102, 0.850631)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0535525, 0.996063, 0.0706384)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.528153, -0.0325149, 0.848527)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0536469, 0.995993, 0.0715574)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.531515, -0.0329168, 0.846409)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0537377, 0.995921, 0.0724767)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.534869, -0.033316, 0.844278)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0538248, 0.995849, 0.0733963)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.538215, -0.0337124, 0.842133)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0539083, 0.995777, 0.0743163)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.541552, -0.034106, 0.839975)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0539881, 0.995703, 0.0752365)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.544881, -0.0344968, 0.837804)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0540642, 0.995629, 0.0761569)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.548201, -0.0348848, 0.835618)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0541367, 0.995554, 0.0770776)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.551513, -0.0352699, 0.83342)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0542055, 0.995479, 0.0779985)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.554817, -0.0356523, 0.831208)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0542706, 0.995403, 0.0789196)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.558112, -0.0360319, 0.828983)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0543321, 0.995326, 0.079841)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.561398, -0.0364086, 0.826745)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0543898, 0.995248, 0.0807625)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.564675, -0.0367825, 0.824493)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.054444, 0.99517, 0.0816841)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.567944, -0.0371536, 0.822228)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0544944, 0.995091, 0.0826059)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.571203, -0.0375218, 0.819951)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0545412, 0.995012, 0.0835279)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.574454, -0.0378872, 0.817659)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0545843, 0.994932, 0.08445)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.577696, -0.0382497, 0.815355)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0546237, 0.994851, 0.0853722)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.580929, -0.0386094, 0.813038)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0546594, 0.994769, 0.0862944)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.584153, -0.0389662, 0.810708)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0546915, 0.994687, 0.0872168)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.587368, -0.0393201, 0.808365)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0547199, 0.994604, 0.0881392)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.590573, -0.0396711, 0.806008)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0547446, 0.994521, 0.0890616)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.59377, -0.0400193, 0.803639)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0547656, 0.994436, 0.0899841)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.596957, -0.0403646, 0.801257)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0547829, 0.994351, 0.0909066)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.600134, -0.0407069, 0.798863)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0547966, 0.994266, 0.0918291)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.603303, -0.0410464, 0.796455)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0548066, 0.99418, 0.0927516)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.606462, -0.041383, 0.794035)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0548129, 0.994093, 0.0936741)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.609612, -0.0417166, 0.791602)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0548156, 0.994005, 0.0945965)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.612752, -0.0420474, 0.789156)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0548145, 0.993917, 0.0955188)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.615882, -0.0423752, 0.786698)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0548098, 0.993828, 0.0964411)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.619003, -0.0427001, 0.784227)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0548014, 0.993739, 0.0973633)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.622114, -0.043022, 0.781744)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0547893, 0.993649, 0.0982854)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.625216, -0.043341, 0.779248)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0547736, 0.993558, 0.0992074)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.628307, -0.0436571, 0.776739)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0547541, 0.993467, 0.100129)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.631389, -0.0439702, 0.774219)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.054731, 0.993375, 0.101051)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.634461, -0.0442804, 0.771685)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0547042, 0.993282, 0.101972)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.637523, -0.0445876, 0.76914)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0546738, 0.993189, 0.102894)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.640575, -0.0448918, 0.766582)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0546396, 0.993095, 0.103815)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.643617, -0.0451931, 0.764012)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0546018, 0.993, 0.104736)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.646649, -0.0454914, 0.76143)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0545603, 0.992905, 0.105657)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.649671, -0.0457867, 0.758835)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0545151, 0.992809, 0.106577)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.652683, -0.0460791, 0.756228)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0544663, 0.992712, 0.107497)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.655685, -0.0463684, 0.75361)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0544137, 0.992615, 0.108417)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.658676, -0.0466548, 0.750979)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0543575, 0.992517, 0.109337)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.661657, -0.0469381, 0.748336)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0542977, 0.992419, 0.110256)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.664627, -0.0472185, 0.745681)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0542341, 0.99232, 0.111175)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.667588, -0.0474958, 0.743015)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0541669, 0.99222, 0.112094)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.670537, -0.0477702, 0.740336)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0540961, 0.99212, 0.113012)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.673476, -0.0480415, 0.737646)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0540215, 0.992019, 0.11393)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.676405, -0.0483098, 0.734944)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0539433, 0.991917, 0.114848)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.679323, -0.0485751, 0.73223)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0538614, 0.991815, 0.115765)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.682231, -0.0488373, 0.729504)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0537759, 0.991712, 0.116682)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.685127, -0.0490966, 0.726767)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0536867, 0.991609, 0.117599)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.688013, -0.0493527, 0.724018)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0535938, 0.991505, 0.118515)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.690888, -0.0496059, 0.721258)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0534973, 0.9914, 0.11943)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.693753, -0.049856, 0.718486)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0533971, 0.991295, 0.120345)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.696606, -0.050103, 0.715702)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0532933, 0.991189, 0.12126)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.699448, -0.050347, 0.712907)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0531858, 0.991083, 0.122174)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.70228, -0.0505879, 0.710101)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0530747, 0.990976, 0.123088)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.7051, -0.0508258, 0.707284)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0529599, 0.990868, 0.124001)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.70791, -0.0510606, 0.704455)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0528414, 0.99076, 0.124913)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.710708, -0.0512923, 0.701615)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0527194, 0.990651, 0.125825)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.713495, -0.051521, 0.698763)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0525936, 0.990541, 0.126737)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.716271, -0.0517466, 0.695901)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0524643, 0.990431, 0.127648)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.719036, -0.0519691, 0.693027)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0523312, 0.99032, 0.128558)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.721789, -0.0521885, 0.690142)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0521946, 0.990209, 0.129467)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.724531, -0.0524048, 0.687247)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0520543, 0.990097, 0.130376)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.727262, -0.052618, 0.68434)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0519104, 0.989985, 0.131285)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.729981, -0.0528282, 0.681423)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0517628, 0.989872, 0.132193)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.732689, -0.0530352, 0.678494)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0516116, 0.989758, 0.1331)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.735385, -0.0532392, 0.675555)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0514568, 0.989644, 0.134006)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.73807, -0.05344, 0.672605)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0512984, 0.989529, 0.134912)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.740743, -0.0536377, 0.669644)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0511363, 0.989413, 0.135817)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.743404, -0.0538324, 0.666673)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0509706, 0.989297, 0.136721)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.746054, -0.0540239, 0.66369)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0508013, 0.989181, 0.137624)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.748692, -0.0542123, 0.660698)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0506284, 0.989064, 0.138527)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.751318, -0.0543975, 0.657695)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0504519, 0.988946, 0.139429)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.753932, -0.0545797, 0.654681)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0502718, 0.988828, 0.14033)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.756535, -0.0547587, 0.651657)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.050088, 0.988709, 0.14123)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.759126, -0.0549346, 0.648622)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0499007, 0.988589, 0.14213)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.761704, -0.0551073, 0.645577)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0497098, 0.988469, 0.143029)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.764271, -0.0552769, 0.642522)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0495152, 0.988349, 0.143926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.766825, -0.0554434, 0.639457)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0493171, 0.988228, 0.144823)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.769368, -0.0556068, 0.636381)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0491154, 0.988106, 0.14572)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.771898, -0.055767, 0.633295)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0489101, 0.987984, 0.146615)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.774417, -0.055924, 0.630199)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0487012, 0.987861, 0.147509)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.776923, -0.0560779, 0.627094)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0484887, 0.987738, 0.148403)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.779417, -0.0562287, 0.623978)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0482727, 0.987614, 0.149295)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.781898, -0.0563763, 0.620852)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0480531, 0.987489, 0.150186)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.784367, -0.0565207, 0.617716)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0478299, 0.987364, 0.151077)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.786824, -0.056662, 0.614571)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0476031, 0.987239, 0.151967)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.789269, -0.0568001, 0.611415)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0473728, 0.987113, 0.152855)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.791701, -0.0569351, 0.60825)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.047139, 0.986986, 0.153743)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.79412, -0.0570669, 0.605076)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0469015, 0.986859, 0.154629)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.796527, -0.0571955, 0.601891)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0466606, 0.986731, 0.155515)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.798922, -0.057321, 0.598697)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.046416, 0.986603, 0.156399)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.801304, -0.0574432, 0.595494)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.046168, 0.986474, 0.157283)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.803673, -0.0575624, 0.592281)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0459164, 0.986345, 0.158165)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.806029, -0.0576783, 0.589058)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0456613, 0.986215, 0.159046)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.808373, -0.0577911, 0.585827)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0454026, 0.986084, 0.159926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810704, -0.0579006, 0.582586)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0451404, 0.985953, 0.160805)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.813023, -0.058007, 0.579335)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0448747, 0.985822, 0.161683)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.815328, -0.0581103, 0.576076)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0446055, 0.98569, 0.16256)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.817621, -0.0582103, 0.572807)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0443327, 0.985557, 0.163435)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.8199, -0.0583072, 0.569529)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0440565, 0.985424, 0.16431)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.822167, -0.0584008, 0.566242)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0437767, 0.985291, 0.165183)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.824421, -0.0584913, 0.562947)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0434934, 0.985157, 0.166055)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.826662, -0.0585786, 0.559642)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0432067, 0.985022, 0.166926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.82889, -0.0586627, 0.556328)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0429165, 0.984887, 0.167795)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.831104, -0.0587436, 0.553005)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0426227, 0.984752, 0.168663)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.833306, -0.0588213, 0.549674)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0423255, 0.984616, 0.16953)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.835494, -0.0588958, 0.546334)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0420248, 0.984479, 0.170396)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.837669, -0.0589671, 0.542985)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0417207, 0.984342, 0.17126)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.839831, -0.0590352, 0.539628)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0414131, 0.984204, 0.172124)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.84198, -0.0591001, 0.536262)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.041102, 0.984066, 0.172985)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.844115, -0.0591618, 0.532888)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0407875, 0.983928, 0.173846)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

ToggleSpinMode()

LEN = 20
i = 0
while i <= LEN:
    SetTimeSliderState(i)
    sw.fileName="frames/m%02d" %(frame_idx)
    frame_idx = frame_idx+1
    SetSaveWindowAttributes(sw)
    MySaveWindow()
    Slow()
    i += 1

RestoreSession("/Users/sarahgreenlaw/Documents/CIS410/label.session", 0)
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.844115, -0.0591618, 0.532888)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0407875, 0.983928, 0.173846)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)

sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
PauseFewSeconds()

RestoreSession("/Users/sarahgreenlaw/Documents/CIS410/contour.session", 0)
SetTimeSliderState(20)

# Begin
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.844115, -0.0591618, 0.532888)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0407875, 0.983928, 0.173846)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

LEN = 160
i = 20
while i <= LEN:
    SetTimeSliderState(i)
    sw.fileName="frames/m%02d" %(frame_idx)
    frame_idx = frame_idx+1
    SetSaveWindowAttributes(sw)
    MySaveWindow()
    Slow()
    i += 1

RestoreSession("/Users/sarahgreenlaw/Documents/CIS410/vectorlabel.session", 0)
SetTimeSliderState(1)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()
PauseFewSeconds()



RestoreSession("/Users/sarahgreenlaw/Documents/CIS410/vector1.session", 0)
SetTimeSliderState(1)
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.844115, -0.0591618, 0.532888)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0407875, 0.983928, 0.173846)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

LEN = 60
i = 1
while i <= LEN:
    SetTimeSliderState(i)
    sw.fileName="frames/m%02d" %(frame_idx)
    frame_idx = frame_idx+1
    SetSaveWindowAttributes(sw)
    MySaveWindow()
    Slow()
    i += 1

RestoreSession("/Users/sarahgreenlaw/Documents/CIS410/vector2.session", 0)
ResetView()
SetTimeSliderState(1)
sw.fileName="frames/m%02d" %(frame_idx)
frame_idx = frame_idx+1
SetSaveWindowAttributes(sw)
MySaveWindow()

LEN = 19
i = 1
while i <= LEN:
    SetTimeSliderState(i)
    Pause()
#    sw.fileName="frames/m%02d" %(frame_idx)
#    frame_idx = frame_idx+1
#    SetSaveWindowAttributes(sw)
#    MySaveWindow()
    i += 1
RestoreSession("/Users/sarahgreenlaw/Documents/CIS410/vector2label.session", 0)
PauseFewSeconds()
RestoreSession("/Users/sarahgreenlaw/Documents/CIS410/vector2.session", 0)
SetTimeSliderState(19)
ToggleSpinMode()
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.176171, 0.28057, 0.943528)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.154435, 0.938771, -0.307991)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.169606, 0.302728, 0.937864)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.149959, 0.932643, -0.328161)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.162928, 0.32471, 0.931675)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.145624, 0.926036, -0.348211)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.15614, 0.346504, 0.924962)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.141433, 0.918955, -0.368129)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.149247, 0.368099, 0.91773)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.137388, 0.911403, -0.387904)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.142252, 0.38948, 0.909983)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.133492, 0.903385, -0.407524)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.135158, 0.410638, 0.901726)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.129746, 0.894905, -0.426979)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.127971, 0.431558, 0.892962)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.126152, 0.885968, -0.446257)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.120694, 0.45223, 0.883697)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.122714, 0.87658, -0.465348)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.113331, 0.472643, 0.873936)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.119432, 0.866745, -0.484241)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.105887, 0.492783, 0.863686)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.116308, 0.856469, -0.502925)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0983658, 0.51264, 0.85295)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.113345, 0.845758, -0.521389)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0907713, 0.532203, 0.841737)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.110544, 0.834618, -0.539623)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0831081, 0.551461, 0.830051)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.107906, 0.823055, -0.557617)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0753804, 0.570402, 0.8179)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.105433, 0.811076, -0.57536)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0675928, 0.589016, 0.80529)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.103127, 0.798688, -0.592843)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0597496, 0.607292, 0.792229)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.100988, 0.785897, -0.610055)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0518553, 0.62522, 0.778724)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0990185, 0.772711, -0.626987)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0439143, 0.64279, 0.764782)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0972189, 0.759138, -0.643629)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0359311, 0.659993, 0.750412)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0955904, 0.745185, -0.659972)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0279103, 0.676817, 0.735622)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.094134, 0.730859, -0.676006)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0198564, 0.693253, 0.72042)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0928503, 0.71617, -0.691722)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0117739, 0.709293, 0.704815)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0917403, 0.701125, -0.707112)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.00366752, 0.724928, 0.688815)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0908044, 0.685733, -0.722167)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.00445825, 0.740147, 0.67243)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0900433, 0.670003, -0.736878)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0125988, 0.754943, 0.655669)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0894573, 0.653943, -0.751237)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

ToggleSpinMode()
ToggleSpinMode()
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.00854357, 0.738628, 0.674059)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.08887, 0.671977, -0.735221)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0041543, 0.724288, 0.689485)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0884487, 0.687055, -0.721202)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.000243039, 0.709613, 0.704592)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0881179, 0.701836, -0.706867)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.00464641, 0.69461, 0.719372)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0878776, 0.716313, -0.692224)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.00905377, 0.679287, 0.733817)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0877281, 0.730478, -0.677278)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0134631, 0.66365, 0.747922)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0876694, 0.744326, -0.662037)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0178723, 0.647707, 0.76168)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0877015, 0.75785, -0.646507)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0222794, 0.631465, 0.775085)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0878244, 0.771044, -0.630697)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0266823, 0.614931, 0.788129)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.088038, 0.783901, -0.614613)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.031079, 0.598114, 0.800808)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0883423, 0.796416, -0.598262)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0354675, 0.581021, 0.813116)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.088737, 0.808583, -0.581653)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0398457, 0.56366, 0.825046)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0892221, 0.820396, -0.564792)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0442116, 0.546038, 0.836593)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0897973, 0.83185, -0.547688)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0485631, 0.528165, 0.847752)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0904623, 0.842939, -0.530349)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0528983, 0.510049, 0.858517)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0912168, 0.853659, -0.512783)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0572152, 0.491697, 0.868885)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0920605, 0.864004, -0.494997)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0615117, 0.473119, 0.878849)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.092993, 0.87397, -0.477001)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0657859, 0.454322, 0.888405)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0940138, 0.883551, -0.458801)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0700357, 0.435316, 0.897549)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0951225, 0.892744, -0.440408)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0742593, 0.416109, 0.906277)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0963186, 0.901545, -0.421829)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0784547, 0.396711, 0.914585)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0976014, 0.909949, -0.403073)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0826198, 0.37713, 0.922468)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.0989705, 0.917952, -0.384148)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0867529, 0.357376, 0.929923)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.100425, 0.92555, -0.365064)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0908519, 0.337457, 0.936947)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.101965, 0.932741, -0.345829)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.094915, 0.317382, 0.943536)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.103588, 0.93952, -0.326452)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0989403, 0.297162, 0.949687)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.105296, 0.945885, -0.306942)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.102926, 0.276805, 0.955398)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.107086, 0.951833, -0.287309)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.10687, 0.256321, 0.960666)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.108957, 0.957361, -0.26756)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.110771, 0.235719, 0.965488)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.11091, 0.962466, -0.247706)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.114627, 0.215009, 0.969862)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.112943, 0.967146, -0.227755)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.118435, 0.1942, 0.973786)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.115054, 0.971399, -0.207718)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.122195, 0.173303, 0.977259)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.117244, 0.975223, -0.187602)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.125905, 0.152326, 0.980278)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.119511, 0.978616, -0.167418)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.129562, 0.13128, 0.982842)
View3DAtts.focus = (0.29246, 0.29146, 0.219095)
View3DAtts.viewUp = (-0.121854, 0.981576, -0.147174)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.469765
View3DAtts.nearPlane = -0.93953
View3DAtts.farPlane = 0.93953
View3DAtts.imagePan = (-0.114232, 0.0834473)
View3DAtts.imageZoom = 3.27803
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0.29246, 0.29146, 0.219095)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
Pause()
Pause()
ToggleSpinMode()

LEN = 160
i = 19
ResetView()
while i <= LEN:
    SetTimeSliderState(i)
    sw.fileName="frames/m%02d" %(frame_idx)
    frame_idx = frame_idx+1
    SetSaveWindowAttributes(sw)
    MySaveWindow()
    Slow()
    i += 1


RestoreSession("/Users/sarahgreenlaw/Documents/CIS410/blank.session", 0)
PauseFewSeconds()
