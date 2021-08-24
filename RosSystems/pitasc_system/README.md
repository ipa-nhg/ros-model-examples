## Commands:

```
docker run -it haros_melodic:latest /haros_runner.sh optoforce_etherdaq_driver etherdaq_node node . /root/ws "https://github.com/ptenbrock/etherdaq_ros -b tare_srv" 

docker run -it haros_melodic:latest /haros_runner.sh optoforce_etherdaq_driver etherdaq_subscriber node . /root/ws "https://github.com/ptenbrock/etherdaq_ros -b tare_srv"

docker run -it haros_melodic:latest /haros_runner.sh ipa325_wsg50 schunk_gripper node . /root/ws https://github.com/ipa-jsk/ipa325_wsg50
 
docker run -it haros_melodic:latest /haros_runner.sh robotiq_ft_sensor rq_sensor node . /root/ws https://github.com/ros-industrial/robotiq
 
RosCommonObjects/de.fraunhofer.ipa.ros.communication.objects/basic_msgs/generate_messages_model_helper.sh robotiq_ft_sensor
 
RosCommonObjects/de.fraunhofer.ipa.ros.communication.objects/basic_msgs/generate_messages_model_helper.sh ipa325_wsg50

```

Extractors from: https://github.com/ipa320/ros-model-extractors