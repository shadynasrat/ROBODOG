# SPDX-FileCopyrightText: Copyright (c) 2021 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright (c) 2021 ETH Zurich, Nikita Rudin

from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class SoloFlatCfg( LeggedRobotCfg ):
    class env( LeggedRobotCfg.env ):
        num_envs = 4096
        num_actions = 3
        num_observations = 21

    class terrain( LeggedRobotCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False
        static_friction = 1.
        dynamic_friction = 1.


    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.0] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            "stand_imu": 0.15,
            "FR_hip_joint": 0.0,
            "FR_thigh_joint": 1.35,
            "FR_calf_joint": -2.5,
        }

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        action_dof_name = ["FR_hip_joint", "FR_thigh_joint", "FR_calf_joint"]
        stiffness = {'FR_hip_joint': 80., 'FR_thigh_joint': 80., 'FR_calf_joint': 80.}  # [N*m/rad]
        damping = {'FR_hip_joint': 2., 'FR_thigh_joint': 2., 'FR_calf_joint': 2.}     # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.5
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4
        use_actuator_network = False
        actuator_net_file = "{LEGGED_GYM_ROOT_DIR}/resources/actuator_nets/anydrive_v3_lstm.pt"
        controller = True

    class asset( LeggedRobotCfg.asset ):
        file = "{LEGGED_GYM_ROOT_DIR}/resources/robots/solo/urdf/solo.urdf"
        name = "solo"
        foot_name = "FOOT"
        penalize_contacts_on = ["FR_hip", "FR_thigh", "FR_calf", "FR_thigh_shoulder"]
        terminate_after_contacts_on = ["FR_hip", "FR_thigh", "FR_calf", "FR_thigh_shoulder"]
        self_collisions = 0 # 1 to disable, 0 to enable...bitwise filter
        flip_visual_attachments = True
        fix_base_link = True

    class domain_rand( LeggedRobotCfg.domain_rand):
        randomize_base_mass = True
        added_mass_range = [-5., 5.]

    class commands( LeggedRobotCfg.commands):
        heading_command = False
        added_mass_range = [-5., 5.]
        num_commands = 1
        class ranges:
            lin_vel_z = [-1.0, 1.0] # min max [m/s]

    class rewards( LeggedRobotCfg.rewards ):
        #base_height_target = 100.
        max_contact_force = 50.
        only_positive_rewards = True
        class scales( LeggedRobotCfg.rewards.scales ):
            lin_vel_z = 0.1
            torques = -0.01
            feet_air_time =  0.0
            action_rate = -0.1
            stand_still = 2

class SoloFlatCfgPPO( LeggedRobotCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'solo_flat'
        load_run = 0
