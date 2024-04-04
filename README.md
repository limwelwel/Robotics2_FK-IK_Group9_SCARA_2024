<p align="center">
  <img src=https://github.com/limwelwel/PYTHON-PROGRAMS/blob/3078971571d8ab959cb3e9882e7a0265d9947afc/bsu%20header.png alt=Bsu style="height: 200px;">
  <hr>
<h3 align="center">COLLEGE OF ENGINEERING</h3>
<h3 align="center">BACHELOR OF SCIENCE IN MECHATRONICS ENGINEERING</h3>
<h3 align="center">ROBOTICS 2: Midterm Project</h3>
<h1 align="center"> Forward and Inverse Kinematics </h1> 
<br>

## I. Abstract of the Project
<p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This project offers an in-depth analysis of an <b>RRP</b> variant <b>SCARA</b> Manipulator, <b><i>Selective Compliance Articulated Robot for Assembly</i></b>. This includes the calculation of the degrees of freedom (DOF).  The use of Denavit-Hartenberg (DH) frame notation, which offers a methodical representation of the interaction between links and joints, is also explored in this section for modeling the kinematics of the SCARA Manipulator. The inverse kinematics will also be presented in this project. Furthermore, the GUI calculator gives assistance in terms of checking if the calculations of various parts of the SCARA manipulator are correct. All the fundamental concepts that have been mentioned were supported through simulation in Python, whereas it can be utilized to operate a wide range of services and programs. Images and additional descriptions are also added to create a more defined illustration of the principles of how a SCARA Manipulator operates.</p>

## II. Introduction of the Project
<p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In 1978, Professor Hiroshi Makino's group at Yamanashi University in Japan created the first **SCARA** <b><i>(Selective Compliance Articulated Robot for Assembly)</i></b> manipulator for use in industry. The initial purpose of SCARA robots was to meet the demand for quick and accurate assembly activities in the manufacturing sector. For a variety of assembly processes, including pick-and-place, assembly, and packaging applications, its mobility is helpful. SCARA robots, which were initially introduced to industrial assembly lines in 1981, continue to provide the finest results for high-speed assembly. The desire to combine the advantages of Cartesian and Articulated robots, allowing for increased reach, flexibility, and precision in assembly tasks, had an impact on the development of SCARA manipulators.
  <p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As technology undergoes rapid advancement, complicated tasks such as control systems are accomplished with a highly automated control system. Due to increased use of industrial robot arms, an evolution to that topic began trying to imitate human movements in a detailed mode. The mechanical design of the robot arm is based on a robot manipulator with similar functions to a human arm. The links of such a manipulator are connected by joints allowing rotational motion and the links of the manipulator are considered to form a kinematic chain. The business end of the kinematic chain of the manipulator is called the end effector or end-of-arm-tooling and it is analogous to the human hand. To validate the right positioning of the robotic arm, inverse kinematics calculations are carried out.

## III. Degrees of Freedom of SCARA Mechanical Manipulaltor
<p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>DOF, or Degrees of Freedom</b>, refers to the number of possible independent variables or parameters that a system or a manipulator can possess. Moreover, it is usually referred to as the number of joints or axes of motion. In a mechanism, three-dimensional space can support up to 6 degrees of freedom, represented as translational and rotational. Whereas, translational motion refers to the movement that is both linear and non-rotational. While rotational motion is referred to as the opposite of translational motion. The SCARA manipulator has a total of 3 degrees of freedom, and it consists of 2 revolute joints and 1 prismatic joint, also referred to as RRP (Revolute-Revolute-Prismatic).
  
<p align="center">
  <a href="https://drive.google.com/file/d/1CdT6I6RHsr7WKCz6EY8NfhsUF3WhsL46/view?usp=sharing"><img alt="Task 1" title="Task 1" src="https://github.com/limwelwel/PYTHON-PROGRAMS/blob/e5505ad3d8627a24d04b4ce95dc09fd4f19ea097/TASK%201.png"/></a>
<h3 align="center"> <b><i>Video 1. Solving the DOF (Degrees of Freedom) of the Standard SCARA Manipulator</i></b> </h3> 
  
## IV. Kinematic Diagram and D-H Frame assignment of SCARA Mechanical Manipulator 
<p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The <b>Denavit-Hartenberg Notation</b> of a specific manipulator can be done with the help of D-H Frame Rules to identify the frames of respective joints, where it serves as the coordinate system of the manipulator to know where it is and where to go. And to be able to do this there are rules that must be followed. Listed below are the D-H Preliminary Rules in identifying the D-H notation of a SCARA manipulator:

### D-H Frame Preliminary Rules

**Rule 1:** Decide first the 3 views you want to project on your isometric drawing..

**Rule 2:** Identify the center of your frames.

**Rule 3:** Draw the color Coded arrows based on your decided 3 views.
(Blue for Z-Axis, Green for Y-Axis, and Red for X-Axis)

**Rule 4:** remember to make the arrows of Z and X axes easy to see for the future computations.

<p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The actual assignment of the frames can be a help for a much easier approach of analyzing the manipulator’s kinematic behavior. Rules are to be considered as well for an organized and systematic identification of the frames for specific joints, either revolute or prismatic.

### D-H Frame Rules

**Rule 1:** The Z axis must be the axis of rotation for a revolute/twisting, or the direction of translation for a prismatic joint.

**Rule 2:** The X axis must be perpendicular both to its own Z axis, and the Z axis of the frame before it.

**Rule 3:** Each X axis must intersect the Z axis of the frame before it. If this rule was not followed there are Rules for Complying this 3rd Rule:
- Rotate the axis until it hits the other.
- Or translate the axis until it hits the other.

**Rule 4:** All frames must follow the right-hand rule.

 <p align="center">
  <a href="https://drive.google.com/file/d/1rymezMT4zJorQF2his_l1TRBt6K0IQWT/view?usp=sharing"><img alt="Task 2" title="Task 2" src="https://github.com/limwelwel/DRAFT/blob/8f3403cf6326093505c01075768493b42df13742/TASK%202.png"/></a>
<h3 align="center"> <b><i>Video 2. Assigning of Frames of the Standard SCARA Manipulator</i></b> </h3>
   
## V. D-H Parametric Table of SCARA Mechanical Manipulator
<p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jacques Denavit and Richard Hartenberg introduce a convention called <b>D-H Parametric table</b>, also known as the Denavit-Hartenberg table, a tabular representation that captures the geometric and kinematic properties of each link and joint in a mechanical manipulator. This approach can be used for an efficient analysis, modeling,and control of the mechanical manipulator’s motion. Parameters <b>θ, 𝛂, r</b>, and d are the four important parameters associated with this approach. These parameters employ specific roles and identification. θ (Theta) and 𝛂 (Alpha) are the parameters that describes the rotation or orientation of the manipulator.  r, and d are parameters that can describe the displacement of the subsequent joint to the succeeding joint with respect to an axis.

<p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In fulfilling the necessary values for the D-H Parametric table,  it is important to always take note of the guidelines for finding the values for the respective parameters.

**θ** - This is the Rotation around Zn-1 that us required to get the Xn-1 to match Xn with the joint variable Θ, if joint is revolute / twisting joint.

**⍺** - This is the Rotation around Xn that is required to match Zn-1 to Zn.

**r** - The distance between  the origins of n-1 and n frames along the Xn direction.

**d** - The distance between the origins of n-1 and n frames along the Zn-1 direction, with joint variables if the joint is prismatic.

<p align="center">
  <a href="https://drive.google.com/file/d/1naChFGyDiIW3-L_m8huqTZHfjY5MXMNQ/view?usp=sharing"><img alt="Task 3" title="Task 3" src="https://github.com/limwelwel/DRAFT/blob/8f3403cf6326093505c01075768493b42df13742/TASK%203.png"/></a>
<h3 align="center"> <b><i>Video 3. Obtaining the D-H Parametric Table of the Standard SCARA Manipulator</i></b> </h3>
  
## VI. HTM of SCARA Mechanical Manipulator
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A <b>Homogeneous Transformation Matrix</b>, often used in computer graphics, computer vision, and robotics, is a mathematical representation of a coordinate transformation in a homogeneous coordinate system. It is typically used to describe transformations such as translation, rotation, scaling, and shearing in a single matrix.

  <p align="center">
  <a href="https://drive.google.com/file/d/1oKe80Zd7q9mNZIj_aM2I1ZoP5hwllQgU/view?usp=sharing"><img alt="Task 4" title="Task 4" src="https://github.com/limwelwel/DRAFT/blob/8f3403cf6326093505c01075768493b42df13742/TASK%204.png"/></a>
<h3 align="center"> <b><i>Video 4. Solving the HTM (Homogeneous Transformation Matrix) of the Standard SCARA Manipulator</i></b> </h3>
    
## VII. Inverse Kinematics of SCARA Mechanical Manipulator
<p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Inverse kinematics</b> is a mathematical process that determines the joint positions required to position a robot's end effector at a specific position and orientation (also known as its "pose"). When dealing with inverse kinematics, there can be multiple solutions and approaches to calculating the desired joint positions. In the case of an RRP SCARA manipulator, which involves finding solutions for joint variables like  θ1, θ2 and d3, the process typically entails visualizing the kinematic diagram from a top view and utilizing mathematical formulas to determine the joint angles. It is important to note that for an RRP SCARA manipulator, seven solutions can be obtained for the inverse kinematics, which is essential in specifying the robot's motion.

<p align="center">
  <a href="https://drive.google.com/file/d/179n20iP9Uhr3h8p6Zi4qoV-yyfQ9ytl5/view?usp=sharing"><img alt="Task 5" title="Task 5" src="https://github.com/limwelwel/DRAFT/blob/8f3403cf6326093505c01075768493b42df13742/TASK%205.png"/></a>
<h3 align="center"> <b><i>Video 5. Solving the Inverse Kinematics of the Standard SCARA Manipulator using Graphical/Geometrical Method</i></b> </h3>

## VIII. Forward and Inverse Kinematics GUI calculator of SCARA Mechanical Manipulator 
<p align="justify"> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This section showcases the different calculators for SCARA manipulators used in Python Simulation. Two types of calculators were used for the simulation: <b>Forward Kinematics Calculator and Inverse Kinematics Calculator</b>.

  <p align="center">
  <a href="https://drive.google.com/file/d/1cS7UrIVmMEwfAtqNzpuIv1ekngvSZmjs/view?usp=sharing"><img alt="Task 5" title="Task 5" src="https://github.com/limwelwel/DRAFT/blob/8f3403cf6326093505c01075768493b42df13742/TASK%206.png"/></a>
<h3 align="center"> <b><i>Video 6. GUI Calculator of the Standard SCARA Manipulator</i></b> </h3>
    
## IX. References

<hr>
<p align="center">
  <img src=https://github.com/limwelwel/PYTHON-PROGRAMS/blob/3078971571d8ab959cb3e9882e7a0265d9947afc/bsu%20footer.png alt=Bsu style="height: 200px;">
