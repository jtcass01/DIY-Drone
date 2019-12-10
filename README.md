# DIY-Drone
Over my Christmas break I have decided to build a drone from parts.  This Repo will likely involve overtime as I better understand what I want to do with the drone.  My first idea is write an object following algorithm.  I'd also like to replace the Navio2 with controllers that I design.  I can't afford a physical controller right now.  I hope to simulate one with a computer.

## Parts and Current Costs

|                   | Parts List                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |        |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Microcomputer     | [Raspberry Pi 4 2 GB RAM](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27/ref=asc_df_B07TD42S27/?tag=hyprod-20&amp;linkCode=df0&amp;hvadid=380013417597&amp;hvpos=1o3&amp;hvnetw=g&amp;hvrand=1871603270888978787&amp;hvpone=&amp;hvptwo=&amp;hvqmt=&amp;hvdev=c&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9014231&amp;hvtargid=aud-801381245258:pla-774661502856&amp;psc=1&amp;tag=&amp;ref=&amp;adgrpid=77922879259&amp;hvpone=&amp;hvptwo=&amp;hvadid=380013417597&amp;hvpos=1o3&amp;hvnetw=g&amp;hvrand=1871603270888978787&amp;hvqmt=&amp;hvdev=c&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9014231&amp;hvtargid=aud-801381245258:pla-774661502856) | $47.49 |
| Flight Controller | [Navio2 Autopilot HAT](https://emlid.com/navio/)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | $168   |
| Camera            | [Raspberry pi Camera Day &amp; Night Vision, IR-Cut Video Camera 1080p HD Webcam 5MP OV5647 Sensor for Raspberry Pi RPi 4 3 B B+ 2B 3A+ 2 1 Zero W by Longruner](https://www.amazon.com/dp/B07VSPSNL8/?coliid=I3FU1X3S4RPRON&amp;colid=3BXDQII4IRZH1&amp;psc=1&amp;ref_=lv_ov_lig_dp_it)                                                                                                                                                                                                                                                                                                                                                                                        | $27.99 |
| Frame             | [Readytosky S500 Quadcopter Frame Stretch X FPV Drone Frame Kit PCB Version with Carbon Fiber Landing Gear](https://www.amazon.com/dp/B01N0AX1MZ/?coliid=I2HPMUBE963X82&amp;colid=3BXDQII4IRZH1&amp;psc=1&amp;ref_=lv_ov_lig_dp_it)                                                                                                                                                                                                                                                                                                                                                                                                                                             | $46.99 |
| Motors            | [LHI 4x 2212 920KV Brushless Motor (CW / CCW) + 4x SIMONK 30A ESC For DJI Phantom](https://www.amazon.com/dp/B00XQYTZQ2/?coliid=I1V5S3V0ZT9EJN&amp;colid=3BXDQII4IRZH1&amp;psc=1&amp;ref_=lv_ov_lig_dp_it)                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | $53.99 |
| Props             | [RAYCorp® 1045 10x4.5 Propellers. 8 Pieces(4 CW, 4 CCW) Black &amp; Red High Quality 10-inch Quadcopter and Multirotors Props + Battery strap](https://www.amazon.com/dp/B01CJMJ886/?coliid=IK2QO5PJ7H8UR&amp;colid=3BXDQII4IRZH1&amp;psc=1&amp;ref_=lv_ov_lig_dp_it)                                                                                                                                                                                                                                                                                                                                                                                                           | $9.99  |
| Telemetry         | [Readytosky 3DR Radio Telemetry Kit 915Mhz 100mW Air + Ground Module Open Source for Standard Version APM2.6 APM2.8 pixhawk 2.4.6 2.4.8 Flight Controller](https://www.amazon.com/dp/B01DHV4DVA/?coliid=I39ZUSNICOWCP5&amp;colid=3BXDQII4IRZH1&amp;psc=1&amp;ref_=lv_ov_lig_dp_it)                                                                                                                                                                                                                                                                                                                                                                                              | $24.99 |
| PPM Encoder       | [ShareGoo 8CH PPM Encoder &amp; Pixhawk I2C Splitter Expand Module for Pixhawk PPZ MK MWC MegaPirate APM Flight Controller](https://www.amazon.com/dp/B00WJJG8YW/?coliid=I36567AF25ONJO&amp;colid=3BXDQII4IRZH1&amp;psc=1&amp;ref_=lv_ov_lig_dp_it)                                                                                                                                                                                                                                                                                                                                                                                                                             | $12.99 |
| SD Card           | [Kingston Canvas Select 32GB microSDHC Class 10 microSD Memory Card UHS-I 80MB/s R Flash Memory Card with Adapter (SDCS/32GB)](https://www.amazon.com/dp/B079GTYCW4/?coliid=I27XS6A8O1QLJS&amp;colid=3BXDQII4IRZH1&amp;psc=1&amp;ref_=lv_ov_lig_dp_it)                                                                                                                                                                                                                                                                                                                                                                                                                          | $4.95  |
| Battery           | [GOLDBAT 3S 11.1V 3000mAh 30C Lipo Battery with Dean-Style T Connector and XT60 Connector for RC Car Airplane Helicopter Boat Drone FPV and Quadcopter Remote Control Toys](https://www.amazon.com/dp/B07LGZ3TVM/?coliid=I22NTYRSGGSFSE&amp;colid=3BXDQII4IRZH1&amp;psc=1&amp;ref_=lv_ov_lig_dp_it)                                                                                                                                                                                                                                                                                                                                                                             | $22.99 |
| Battery Charger   | [HOBBYMATE Imax B6 Clone Lipo Battery Balance Charger, Rc Hobby Battery Balance Charger LED W/ AC Power Adapter](https://www.amazon.com/dp/B01NB9A36R/?coliid=I1KC117NRYRDYS&amp;colid=3BXDQII4IRZH1&amp;psc=1&amp;ref_=lv_ov_lig_dp_it)                                                                                                                                                                                                                                                                                                                                                                                                                                        | $34.90 |

### Total Cost: $455.27
