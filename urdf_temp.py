

def create_URDF(name, 
                hip, 
                knee, 
                shoulder, 
                elbow, 
                clavicle,
                shoulder_flex_R,
                shoulder_exten_R,
                shoulder_in_R,
                shoulder_out_R,
                elbow_flex_R,
                elbow_exten_R,
                shoulder_flex_L,
                shoulder_exten_L,
                shoulder_in_L,
                shoulder_out_L,
                elbow_flex_L,
                elbow_exten_L,
                posterior_out_R,
                posterior_in_R,
                knee_flex_R,
                posterior_out_L,
                posterior_in_L,
                knee_flex_L,
                knee_str_L,
                knee_str_R,
                shoulder_str_L,
                shoulder_str_R,
                elbow_str_L,
                elbow_str_R,
                hip_joint_str_L,
                hip_joint_str_R,
                upper_eight_Kg,
                row_eight_Kg,
                upper_leg_Avg,
                row_leg_Avg,
                chest_Avg,
                waist_Avg,
                root_Avg
                ) :

    '''
        urdf 파일을 생성하는 함수입니다.
    '''

    #특정 부위의 경우 위치가 달라지게 되면 달라진만큼 offset을 주어 위치시켜주어야 합니다.
    #해당 값은 수정하지 않으시는게 좋습니다.
    j_knee = (hip + knee - 0.2) * -1
    hip_interval = ((hip/2)+0.05) * -1
    j_ankle = (knee + 0.09) * -1
    shoulder_interval = ((shoulder/2) + 0.05)*-1
    j_elbow = (shoulder + elbow - 0.12) * -1
    wrist = (elbow + (0.05*2)) * -1
    clavicle_left = clavicle * -1


    urdf = '''<?xml version="1.0" ?>
            <robot name="{0}">
            <material name="orange">
                <color rgba="1.0 0.4235294117647059 0.0392156862745098 1.0"/>
            </material>
            <link name="base_link">
                </link>
            <link name="base">
                </link>
            <joint name="j_base_base_link_rotation" type="fixed">
                <parent link="base_link"/>
                <child link="base"/>
                <origin rpy="1.5707963267948966 0 0" xyz="0 0 0"/>
            </joint>
            <link name="root">
                <inertial>
                <origin rpy="0 0 0" xyz="0.0 0.07 0.0"/>
                <mass value="{51}"/>
                <inertia ixx="0.019440000000000002" ixy="0" ixz="0" iyy="0.019440000000000002" iyz="0" izz="0.019440000000000002"/>
                </inertial>
                <collision>
                <origin rpy="0 0 0" xyz="0.000000 0.070000 0.000000"/>
                <geometry>
                    <sphere radius="0.09"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="0 0 0" xyz="0.000000 0.070000 0.000000"/>
                <geometry>
                    <sphere radius="0.09"/>
                </geometry>
                </visual>
            </link>
            <joint name="j_root" type="fixed">
                <parent link="base"/>
                <child link="root"/>
                <origin rpy="0 0 0" xyz="0 0.000000 0.000000"/>
            </joint>
            <link name="chest">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 0.120000 0.000000"/>
                <mass value="{49}"/>
                <inertia ixx="0.06776000000000001" ixy="0" ixz="0" iyy="0.06776000000000001" iyz="0" izz="0.06776000000000001"/>
                </inertial>
                <collision>
                <origin rpy="0 0 0" xyz="0.000000 0.120000 0.000000"/>
                <geometry>
                    <sphere radius="0.11"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="0 0 0" xyz="0.000000 0.120000 0.000000"/>
                <geometry>
                    <sphere radius="0.11"/>
                </geometry>
                </visual>
            </link>
            <link name="root_chest_link1">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
            </link>
            <joint name="j_root_chest_joint1" type="revolute">
                <origin rpy="0 0 0" xyz="0.0 0.236151 0.000000"/>
                <parent link="root"/>
                <child link="root_chest_link1"/>
                <axis xyz="1 0 0"/>
                <limit effort="200" lower="-1.2" upper="1.2" velocity="3"/>
            </joint>
            <link name="root_chest_link2">
                <inertial>
                <mass value="{50}"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
                <visual>
                <geometry>
                    <sphere radius="0.05"/>
                </geometry>
                <material name="orange"/>
                </visual>
            </link>
            <joint name="j_root_chest_joint2" type="revolute">
                <parent link="root_chest_link1"/>
                <child link="root_chest_link2"/>
                <axis xyz="0 1 0"/>
                <limit effort="200" lower="-1.2" upper="1.2" velocity="3"/>
            </joint>
            <joint name="j_root_chest_joint3" type="revolute">
                <parent link="root_chest_link2"/>
                <child link="chest"/>
                <axis xyz="0 0 1"/>
                <limit effort="200" lower="-1.2" upper="1.2" velocity="3"/>
            </joint>
            <link name="neck">
                <inertial>
                <origin rpy="0 0 0" xyz="0.0 0.175 0.0"/>
                <mass value="2.000000"/>
                <inertia ixx="0.008405" ixy="0" ixz="0" iyy="0.008405" iyz="0" izz="0.008405"/>
                </inertial>
                <collision>
                <origin rpy="0 0 0" xyz="0.0 0.175 0.0"/>
                <geometry>
                    <sphere radius="0.1025"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="0 0 0" xyz="0.0 0.175 0.0"/>
                <geometry>
                    <sphere radius="0.1025"/>
                </geometry>
                </visual>
            </link>
            <link name="chest_neck_link1">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
            </link>
            <joint name="j_chest_neck_joint1" type="revolute">
                <origin rpy="0 0 0" xyz="0.000000 0.223894 0.000000"/>
                <parent link="chest"/>
                <child link="chest_neck_link1"/>
                <axis xyz="1 0 0"/>
                <limit effort="50" lower="-1" upper="1" velocity="3"/>
            </joint>
            <link name="chest_neck_link2">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
                <visual>
                <geometry>
                    <sphere radius="0.05"/>
                </geometry>
                <material name="orange"/>
                </visual>
            </link>
            <joint name="j_chest_neck_joint2" type="revolute">
                <parent link="chest_neck_link1"/>
                <child link="chest_neck_link2"/>
                <axis xyz="0 1 0"/>
                <limit effort="50" lower="-1" upper="1" velocity="3"/>
            </joint>
            <joint name="j_chest_neck_joint3" type="revolute">
                <parent link="chest_neck_link2"/>
                <child link="neck"/>
                <axis xyz="0 0 1"/>
                <limit effort="50" lower="-1" upper="1" velocity="3"/>
            </joint>
            <link name="right_hip">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 -0.210000 0.000000"/>
                <mass value="{58}"/>
                <inertia ixx="0.037153124999999995" ixy="0.0" ixz="0.0" iyy="0.037153124999999995" iyz="0.0" izz="0.00680625"/>
                </inertial>
                <collision>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.210000 0.000000"/>
                <geometry>
                    <cylinder length="0.22499999999999998" radius="0.0275"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 {7} 0.000000"/>
                <geometry>
                    <cylinder length="{6}" radius="0.055"/>
                </geometry>
                </visual>
            </link>
            <link name="root_right_hip_link1">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
            </link>
            <joint name="j_root_right_hip_joint1" type="revolute">
                <origin rpy="0 0 0" xyz="0.000000 0.000000 0.084887"/>
                <parent link="root"/>
                <child link="root_right_hip_link1"/>
                <axis xyz="1 0 0"/>
                <limit effort="200" lower="-1.5" upper="1.5" velocity="3"/>
            </joint>
            <link name="root_right_hip_link2">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
                <visual>
                <geometry>
                    <sphere radius="0.05"/>
                </geometry>
                <material name="orange"/>
                </visual>
            </link>
            <joint name="j_root_right_hip_joint2" type="revolute">
                <parent link="root_right_hip_link1"/>
                <child link="root_right_hip_link2"/>
                <axis xyz="0 1 0"/>
                <limit effort="200" lower="{37}" upper="{38}" velocity="3"/>
            </joint>
            <joint name="j_root_right_hip_joint3" type="revolute">
                <parent link="root_right_hip_link2"/>
                <child link="right_hip"/>
                <axis xyz="0 0 1"/>
                <limit effort="{46}" lower="-1.5" upper="1.5" velocity="3"/>
            </joint>
            <link name="right_knee">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 -0.200000 0.000000"/>
                <mass value="{59}"/>
                <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
                </inertial>
                <collision>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.200000 0.000000"/>
                <geometry>
                    <cylinder length="0.23249999999999998" radius="0.025"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.2 0.000000"/>
                <geometry>
                    <cylinder length="{8}" radius="0.05"/>
                </geometry>
                </visual>
            </link>
            <joint name="j_right_knee" type="revolute">
                <parent link="right_hip"/>
                <child link="right_knee"/>
                <limit effort="{48}" lower="{39}" upper="0." velocity="0.5"/>
                <origin rpy="0 0 0" xyz="0.000000 {9} 0.000000"/>
                <axis xyz="0.000000 0.000000 1.000000"/>
            </joint>
            <link name="right_ankle">
                <inertial>
                <origin rpy="0 0 0" xyz="0.045 -0.00225 0.000000"/>
                <mass value="1.000000"/>
                <inertia ixx="0.0009270833333333333" ixy="0.0" ixz="0.0" iyy="0.0028628333333333327" iyz="0.0" izz="0.003285749999999999"/>
                </inertial>
                <collision>
                <origin rpy="0 0 0" xyz="0.045 -0.00225 0.000000"/>
                <geometry>
                    <box size="0.127 0.055 0.09"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="0 0 0" xyz="0.045 -0.00225 0.000000"/>
                <geometry>
                    <box size="0.127 0.055 0.09"/>
                </geometry>
                </visual>
            </link>
            <joint name="j_right_toe" type="fixed">
                <parent link="right_ankle"/>
                <child link="right_toe"/>
                <limit effort="150.0" lower="-3.14" upper="0." velocity="0.5"/>
                <origin rpy="0 0 0" xyz="0.1 0.0 0.0"/>
                <axis xyz="0.000000 0.000000 1.000000"/>
            </joint>
            <link name="right_toe">
                <inertial>
                <origin rpy="0 0 0" xyz="0.045 0.0 0.0"/>
                <mass value="0.3"/>
                <inertia ixx="0.0009270833333333333" ixy="0.0" ixz="0.0" iyy="0.0028628333333333327" iyz="0.0" izz="0.003285749999999999"/>
                </inertial>
                <collision>
                <origin rpy="0 0 0" xyz="0.045 0.0 0.0"/>
                <geometry>
                    <box size="0.05 0.055 0.09"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="0 0 0" xyz="0.045 0.0 0.0"/>
                <geometry>
                    <box size="0.05 0.055 0.09"/>
                </geometry>
                </visual>
            </link>
            <link name="right_knee_right_ankle_link1">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
            </link>
            <joint name="j_right_knee_right_ankle_joint1" type="revolute">
                <origin rpy="0 0 0" xyz="0.000000 {10} 0.000000"/>
                <parent link="right_knee"/>
                <child link="right_knee_right_ankle_link1"/>
                <axis xyz="1 0 0"/>
                <limit effort="{48}" lower="-1.2" upper="1.2" velocity="3"/>
            </joint>
            <link name="right_knee_right_ankle_link2">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
                <visual>
                <geometry>
                    <sphere radius="0.05"/>
                </geometry>
                <material name="orange"/>
                </visual>
            </link>
            <joint name="j_right_knee_right_ankle_joint2" type="revolute">
                <parent link="right_knee_right_ankle_link1"/>
                <child link="right_knee_right_ankle_link2"/>
                <axis xyz="0 1 0"/>
                <limit effort="90" lower="-1.2" upper="1.2" velocity="3"/>
            </joint>
            <joint name="j_right_knee_right_ankle_joint3" type="revolute">
                <parent link="right_knee_right_ankle_link2"/>
                <child link="right_ankle"/>
                <axis xyz="0 0 1"/>
                <limit effort="90" lower="-1.2" upper="1.2" velocity="3"/>
            </joint>
            <link name="right_shoulder">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 -0.140000 0.000000"/>
                <mass value="{54}"/>
                <inertia ixx="0.004809374999999999" ixy="0.0" ixz="0.0" iyy="0.004809374999999999" iyz="0.0" izz="0.0015187500000000001"/>
                </inertial>
                <collision>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.140000 0.000000"/>
                <geometry>
                    <cylinder length="0.135" radius="0.0225"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 {12} 0.000000"/>
                <geometry>
                    <cylinder length="{11}" radius="0.045"/>
                </geometry>
                </visual>
            </link>
            <link name="chest_right_shoulder_link1">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
            </link>
            <joint name="j_chest_right_shoulder_joint1" type="revolute">
                <origin rpy="0 0 0" xyz="-0.02406 0.24350 {22}"/>
                <parent link="chest"/>
                <child link="chest_right_shoulder_link1"/>
                <axis xyz="1 0 0"/>
                <limit effort="100" lower="{31}" upper="{32}" velocity="3"/>
            </joint>
            <link name="chest_right_shoulder_link2">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
                <visual>
                <geometry>
                    <sphere radius="0.05"/>
                </geometry>
                <material name="orange"/>
                </visual>
            </link>
            <joint name="j_chest_right_shoulder_joint2" type="revolute">
                <parent link="chest_right_shoulder_link1"/>
                <child link="chest_right_shoulder_link2"/>
                <axis xyz="0 1 0"/>
                <limit effort="100" lower="-3.14" upper="3.14" velocity="3"/>
            </joint>
            <joint name="j_chest_right_shoulder_joint3" type="revolute">
                <parent link="chest_right_shoulder_link2"/>
                <child link="right_shoulder"/>
                <axis xyz="0 0 1"/>
                <limit effort="{42}" lower="{29}" upper="{30}" velocity="3"/>
            </joint>
            <link name="right_elbow">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 -0.120000 0.000000"/>
                <mass value="{55}"/>
                <inertia ixx="0.0019187499999999999" ixy="0.0" ixz="0.0" iyy="0.0019187499999999999" iyz="0.0" izz="0.0008"/>
                </inertial>
                <collision>
                <origin rpy="1.5707963267948966 0 0" xyz="0.0 -0.12 0.0"/>
                <geometry>
                    <cylinder length="0.10125" radius="0.02"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="1.5707963267948966 0 0" xyz="0.0 -0.12 0.0"/>
                <geometry>
                    <cylinder length="{13}" radius="0.04"/>
                </geometry>
                </visual>
            </link>
            <joint name="j_right_elbow" type="revolute">
                <parent link="right_shoulder"/>
                <child link="right_elbow"/>
                <limit effort="{44}" lower="{33}" upper="{34}" velocity="0.5"/>
                <origin rpy="0 0 0" xyz="0.000000 {14} 0.000000"/>
                <axis xyz="0.000000 0.000000 1.000000"/>
            </joint>
            <link name="right_wrist">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 0.000000 0.000000"/>
                <mass value="0.500000"/>
                <inertia ixx="0.00032" ixy="0" ixz="0" iyy="0.00032" iyz="0" izz="0.00032"/>
                </inertial>
                <collision>
                <origin rpy="0 0 0" xyz="0.000000 0.000000 0.000000"/>
                <geometry>
                    <sphere radius="0.04"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="0 0 0" xyz="0.000000 0.000000 0.000000"/>
                <geometry>
                    <sphere radius="0.04"/>
                </geometry>
                </visual>
            </link>
            <joint name="j_right_wrist" type="fixed">
                <parent link="right_elbow"/>
                <child link="right_wrist"/>
                <origin rpy="0 0 0" xyz="0.000000 {15} 0.000000"/>
            </joint>
            <link name="left_hip">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 -0.210000 0.000000"/>
                <mass value="{56}"/>
                <inertia ixx="0.037153124999999995" ixy="0.0" ixz="0.0" iyy="0.037153124999999995" iyz="0.0" izz="0.00680625"/>
                </inertial>
                <collision>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.210000 0.000000"/>
                <geometry>
                    <cylinder length="0.22499999999999998" radius="0.0275"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 {2} 0.000000"/>
                <geometry>
                    <cylinder length="{1}" radius="0.055"/>
                </geometry>
                </visual>
            </link>
            <link name="root_left_hip_link1">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
            </link>
            <joint name="j_root_left_hip_joint1" type="revolute">
                <origin rpy="0 0 0" xyz="0.000000 0.000000 -0.084887"/>
                <parent link="root"/>
                <child link="root_left_hip_link1"/>
                <axis xyz="1 0 0"/>
                <limit effort="200" lower="-1.5" upper="1.5" velocity="3"/>
            </joint>
            <link name="root_left_hip_link2">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
                <visual>
                <geometry>
                    <sphere radius="0.05"/>
                </geometry>
                <material name="orange"/>
                </visual>
            </link>
            <joint name="j_root_left_hip_joint2" type="revolute">
                <parent link="root_left_hip_link1"/>
                <child link="root_left_hip_link2"/>
                <axis xyz="0 1 0"/>
                <limit effort="200" lower="{35}" upper="{36}" velocity="3"/>
            </joint>
            <joint name="j_root_left_hip_joint3" type="revolute">
                <parent link="root_left_hip_link2"/>
                <child link="left_hip"/>
                <axis xyz="0 0 1"/>
                <limit effort="{45}" lower="-1.5" upper="1.5" velocity="3"/>
            </joint>
            <link name="left_knee">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 -0.200000 0.000000"/>
                <mass value="{57}"/>
                <inertia ixx="0.025900000000000003" ixy="0.0" ixz="0.0" iyy="0.025900000000000003" iyz="0.0" izz="0.0037500000000000007"/>
                </inertial>
                <collision>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.200000 0.000000"/>
                <geometry>
                    <cylinder length="0.23249999999999998" radius="0.025"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.2 0.000000"/>
                <geometry>
                    <cylinder length="{3}" radius="0.05"/>
                </geometry>
                </visual>
            </link>
            <joint name="j_left_knee" type="revolute">
                <parent link="left_hip"/>
                <child link="left_knee"/>
                <limit effort="{47}" lower="{40}" upper="0." velocity="0.5"/>
                <origin rpy="0 0 0" xyz="0.000000 {4} 0.000000"/>
                <axis xyz="0.000000 0.000000 1.000000"/>
            </joint>
            <link name="left_ankle">
                <inertial>
                <origin rpy="0 0 0" xyz="0.045 -0.00225 0.0"/>
                <mass value="0.7"/>
                <inertia ixx="0.0009270833333333333" ixy="0.0" ixz="0.0" iyy="0.0028628333333333327" iyz="0.0" izz="0.003285749999999999"/>
                </inertial>
                <collision>
                <origin rpy="0 0 0" xyz="0.045 -0.00225 0.0"/>
                <geometry>
                    <box size="0.127 0.055 0.09"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="0 0 0" xyz="0.045 -0.00225 0.0"/>
                <geometry>
                    <box size="0.127 0.055 0.09"/>
                </geometry>
                </visual>
            </link>
            <joint name="j_left_toe" type="fixed">
                <parent link="left_ankle"/>
                <child link="left_toe"/>
                <limit effort="150.0" lower="-3.14" upper="0." velocity="0.5"/>
                <origin rpy="0 0 0" xyz="0.1 0.0 0.0"/>
                <axis xyz="0.000000 0.000000 1.000000"/>
            </joint>
            <link name="left_toe">
                <inertial>
                <origin rpy="0 0 0" xyz="0.045 0.0 0.0"/>
                <mass value="0.3"/>
                <inertia ixx="0.0009270833333333333" ixy="0.0" ixz="0.0" iyy="0.0028628333333333327" iyz="0.0" izz="0.003285749999999999"/>
                </inertial>
                <collision>
                <origin rpy="0 0 0" xyz="0.045 0.0 0.0"/>
                <geometry>
                    <box size="0.05 0.055 0.09"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="0 0 0" xyz="0.045 0.0 0.0"/>
                <geometry>
                    <box size="0.05 0.055 0.09"/>
                </geometry>
                </visual>
            </link>
            <link name="left_knee_left_ankle_link1">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
            </link>
            <joint name="j_left_knee_left_ankle_joint1" type="revolute">
                <origin rpy="0 0 0" xyz="0.000000 {5} 0.000000"/>
                <parent link="left_knee"/>
                <child link="left_knee_left_ankle_link1"/>
                <axis xyz="1 0 0"/>
                <limit effort="90" lower="-1.2" upper="1.2" velocity="3"/>
            </joint>
            <link name="left_knee_left_ankle_link2">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
                <visual>
                <geometry>
                    <sphere radius="0.05"/>
                </geometry>
                <material name="orange"/>
                </visual>
            </link>
            <joint name="j_left_knee_left_ankle_joint2" type="revolute">
                <parent link="left_knee_left_ankle_link1"/>
                <child link="left_knee_left_ankle_link2"/>
                <axis xyz="0 1 0"/>
                <limit effort="90" lower="-1.2" upper="1.2" velocity="3"/>
            </joint>
            <joint name="j_left_knee_left_ankle_joint3" type="revolute">
                <parent link="left_knee_left_ankle_link2"/>
                <child link="left_ankle"/>
                <axis xyz="0 0 1"/>
                <limit effort="90" lower="-1.2" upper="1.2" velocity="3"/>
            </joint>
            <link name="left_shoulder">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 -0.140000 0.000000"/>
                <mass value="{52}"/>
                <inertia ixx="0.004809374999999999" ixy="0.0" ixz="0.0" iyy="0.004809374999999999" iyz="0.0" izz="0.0015187500000000001"/>
                </inertial>
                <collision>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.140000 0.000000"/>
                <geometry>
                    <cylinder length="0.135" radius="0.0225"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 {17} 0.000000"/>
                <geometry>
                    <cylinder length="{16}" radius="0.045"/>
                </geometry>
                </visual>
            </link>
            <link name="chest_left_shoulder_link1">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
            </link>
            <joint name="j_chest_left_shoulder_joint1" type="revolute">
                <origin rpy="0 0 0" xyz="-0.02405 0.24350 {21}"/>
                <parent link="chest"/>
                <child link="chest_left_shoulder_link1"/>
                <axis xyz="1 0 0"/>
                <limit effort="100" lower="{25}" upper="{26}" velocity="3"/>
            </joint>
            <link name="chest_left_shoulder_link2">
                <inertial>
                <mass value="1e-02"/>
                <inertia ixx="1e-02" ixy="0" ixz="0" iyy="1e-02" iyz="0" izz="1e-02"/>
                </inertial>
                <visual>
                <geometry>
                    <sphere radius="0.05"/>
                </geometry>
                <material name="orange"/>
                </visual>
            </link>
            <joint name="j_chest_left_shoulder_joint2" type="revolute">
                <parent link="chest_left_shoulder_link1"/>
                <child link="chest_left_shoulder_link2"/>
                <axis xyz="0 1 0"/>
                <limit effort="100" lower="-3.14" upper="3.14" velocity="3"/>
            </joint>
            <joint name="j_chest_left_shoulder_joint3" type="revolute">
                <parent link="chest_left_shoulder_link2"/>
                <child link="left_shoulder"/>
                <axis xyz="0 0 1"/>
                <limit effort="{41}" lower="{23}" upper="{24}" velocity="3"/>
            </joint>
            <link name="left_elbow">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 -0.12 0.000000"/>
                <mass value="{53}"/>
                <inertia ixx="0.0019187499999999999" ixy="0.0" ixz="0.0" iyy="0.0019187499999999999" iyz="0.0" izz="0.0008"/>
                </inertial>
                <collision>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.12 0.000000"/>
                <geometry>
                    <cylinder length="0.10125" radius="0.02"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="1.5707963267948966 0 0" xyz="0.000000 -0.12 0.000000"/>
                <geometry>
                    <cylinder length="{18}" radius="0.04"/>
                </geometry>
                </visual>
            </link>
            <joint name="j_left_elbow" type="revolute">
                <parent link="left_shoulder"/>
                <child link="left_elbow"/>
                <limit effort="{43}" lower="{27}" upper="{28}" velocity="0.5"/>
                <origin rpy="0 0 0" xyz="0.000000 {19} 0.000000"/>
                <axis xyz="0.000000 0.000000 1.000000"/>
            </joint>
            <link name="left_wrist">
                <inertial>
                <origin rpy="0 0 0" xyz="0.000000 0.000000 0.000000"/>
                <mass value="0.500000"/>
                <inertia ixx="0.00032" ixy="0" ixz="0" iyy="0.00032" iyz="0" izz="0.00032"/>
                </inertial>
                <collision>
                <origin rpy="0 0 0" xyz="0.000000 0.000000 0.000000"/>
                <geometry>
                    <sphere radius="0.04"/>
                </geometry>
                </collision>
                <visual>
                <origin rpy="0 0 0" xyz="0.000000 0.000000 0.000000"/>
                <geometry>
                    <sphere radius="0.04"/>
                </geometry>
                </visual>
            </link>
            <joint name="j_left_wrist_joint" type="fixed">
                <parent link="left_elbow"/>
                <child link="left_wrist"/>
                <origin rpy="0 0 0" xyz="0.000000 {20} 0.000000"/>
            </joint>
            </robot>
            '''.format(name, str(hip),
                        str(hip_interval),
                        str(knee),
                        str(j_knee),
                        str(j_ankle),
                        str(hip),
                        str(hip_interval),
                        str(knee),
                        str(j_knee),
                        str(j_ankle),
                        str(shoulder),
                        str(shoulder_interval),
                        str(elbow), 
                        str(j_elbow),
                        str(wrist),
                        str(shoulder),
                        str(shoulder_interval),
                        str(elbow),
                        str(j_elbow),
                        str(wrist),
                        str(clavicle_left),
                        str(clavicle),
                        str(shoulder_exten_L),
                        str(shoulder_flex_L),
                        str(shoulder_in_L),
                        str(shoulder_out_L),
                        str(elbow_exten_L),
                        str(elbow_flex_L),
                        str(shoulder_exten_R),
                        str(shoulder_flex_R),
                        str(shoulder_out_R),
                        str(shoulder_in_R),
                        str(elbow_exten_R),
                        str(elbow_flex_R),
                        str(posterior_in_L),
                        str(posterior_out_L),
                        str(posterior_in_R),
                        str(posterior_out_R),
                        str(knee_flex_R),
                        str(knee_flex_L),
                        str(shoulder_str_L),
                        str(shoulder_str_R),
                        str(elbow_str_L),
                        str(elbow_str_R),
                        str(hip_joint_str_L),
                        str(hip_joint_str_R),
                        str(knee_str_L),
                        str(knee_str_R),
                        str(chest_Avg),
                        str(waist_Avg),
                        str(root_Avg),
                        str(upper_eight_Kg/2),
                        str(row_eight_Kg/2),
                        str(upper_eight_Kg/2),
                        str(row_eight_Kg/2),
                        str(upper_leg_Avg/2),
                        str(row_leg_Avg/2),
                        str(upper_leg_Avg/2),
                        str(row_leg_Avg/2)
                        )

    return urdf