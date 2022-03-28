# Using Wireless and Thermal Imaging Technology for Lameness Detection


### Introduction 

In Agriculture one of the biggest worries is animal welfare and when we look to one specific area such as the dairy sector we see how animal welfare affects efficiency, productivity and fertility. This is why for this project I proposed a device that detects one of the biggest problems affecting a cows welfare which is lameness since this is something that can go untreated or even undetected it can be the worst problem for cows. As someone who has worked on a farm for many years I know that there aren't many solutions to this problem that actually catch lameness early on before they show actual signs of pain so this is why I decided that this would be the problem I want to try to solve in this project.

### Description
As I stated in the introduction I wanted to come up with a solution that can detect lameness and allow the user to treat the animal before it affects the animals welfare. This will be done through the use of thermal imaging on the cows foot as lameness causes an increase in temperature due to the pain. The end goal for this project is to create an automated system for a milking parlour when the cows enter and their tag number is got and a hoof reading taken so that it can notify the farmer when there is an unusually high temperature caused by lameness. Throughout the project I will use the knowledge I have gained in college and from my work experience but will also learn as much new technologies as possible.

### Inspiration 
Through my experience of working on a dairy farm I know that there are 3 main factors that lower animal welfare and productivity : infertility, mastitis and lameness. Out of the three lameness is the easiest to prevent early on. This is why I thought it would be a good idea to try to come up with a device that could detect it early on. After doing some research I found that there are monitoring systems that use motion sensors but this isn't very efficient for large herds.I found a paper about the use of thermal imaging which led to me using it in this project. After doing more research i found that “lameness is caused by infection (i.e. abscesses, CODD, foot rot) but may also be caused by injury (muscular injuries due to a kick for example), both of which can be identified by increased local temperature using a thermal imaging camera.”(The use of thermal imaging technology to enhance livestock production, 2019)

### Aims
The aims of this project are as follows: 
 - Come up with suitable method/s to detect Lameness in livestock that is affordable and non invasive.
 - Use existing knowledge of hardware, software and IoT platforms that will aid the direction of the end goal.
 - To Alert Users of lameness and relay the information needed to access what method to use to treat the animal.
 - To give users an overview of entire herds through stored data and trend graphs
 - Find Suitable hardware for the project
 - Set up a Thermal Imaging Camera and use the data 
 - Use Radio Frequency Identification to get the tag number of the cows in the herd
 - Create a fully functional android app 

### Methodology 
For the development of this project I've decided to go with the Agile approach. This is conducted through ‘sprints’. At the beginning of the semester I set out my goals and due dates for these sprints, each one allowing for flexibility. 

## Feasibility
### Market
The potential market for this device is huge as many of the options available use more expensive camera set ups or use devices that are on each animal which is accurate but more costly on the farm as more likely to break. “Lameness in dairy cows is a worldwide problem with herd prevalence estimates ranging from 8 % in New Zealand , 22 % in Chile, 32 to 37 % in the UK to 55 % in North America.”(Somers et al., 2015) Lameness is a huge cost on farms as treatment drugs are costly but the aim of my device is to catch it early which can allow for prevention methods such as foot baths, changing their environment and getting a hoof pairer to improve there hoof health. “Thermal Imaging was successfully used in various applications of human and veterinary medicine. In farm animals, IRT cameras have been used to test for early detection of estrus (Hurnik et al., 1985), for mastitis (Berry et al., 2003), for detection of viral diarrhea infections in calves (Schaefer et al., 2007), for cattle infected with foot-and-mouth disease (Rainwater-Lovett et al., 2009), and for evaluating the milking process (Kunc et al., 2007).”(Alsaaod and Büscher, 2012)

### Unique Selling Point 
One of the Key USPs of the project is that it’s a singular device unlike anything currently being sold on the market as most devices use motion detection to record the animals activity and then predict lameness with this data. This works great but in real terms it won’t be implemented in many farms as it’s too costly with the design I have created. A farm can use the point of entry into the milking parlour and place the device there. As each cow enters it can record and detect an increase in hoof temperature which is a sign of lameness and alert the farmer to it which will allow the farmer to treat it before it becomes a problem.

The Another Key USP is that it detects early so in most cases the farmer will be able to use preventive measures rather than actual treatments which is another cost cutting measure that the device gives.

## Key Technologies

### Python
I will be using python as the main language in this project as it is the language I am most comfortable with and yet still haven’t tried anything in this area of the language. I believe it’s the best choice for the project as it contains many image processing libraries such as Scikit-image or OpenCV. I will only be using python to process and send the results which makes it Ideal as I will be using Android to present them to the user.
SQLite
The database I have chosen to use is SQlite as it does not use up  RAM and CPU when not being utilised. As it's a serverless database which is self contained in a file. Since the device won't be storing huge amounts of data it seems like the perfect choice for the early stages of this project.

### Docker
The reason I have chosen to use docker in this project is that I would like to simplify the setup process on the device. It would also be beneficial in the development of the application as I can run and test the whole program without a Raspberry PI with Dummy Data of the thermal camera. I got a lot of experience with docker on my work placement and it is a tool that I feel can be beneficial to the project. By containerizing the program I will make it very simple for others to set up the device. All that will be needed to be done is changes to the configuration file  and installing the camera.

### Grafana
Grafana is an interactive web application that can analyse data sets. I plan to use Grafana to analyse the data of the entire herd and graph herd lameness over a given period of time. I will also use it to implement graphs of individual animals. This will allow the user and I to get a better understanding of temperature trends and make the application more accurate. 

### MQTT
I will be using MQTT to transfer the data between the device and the user interface. I got a lot of experience with MQTT protocols from my work experience. It will allow me to send live results to the user through TCP/IP the reason I chose it is that it can be run on any device as it has low system requirements and all it needs to operate is a internet connection for the project I will most likely create a broker on an AWS/OpenStack Instance which allow for scalability of users.

### Android
I would like to create a mobile app for the user as most users will be farmers on the go and I feel a webpage would be very difficult and extra work for the user to get the results. I haven’t had any experience with Android yet but I do have a module this year. The reason I chose Android is that I know there are a lot of resources available for it and with the knowledge I learned this year I can definitely create a decent user interface. If we look at the users which are mostly farmers most will use android phones.


## Hardware
### Raspberry Pi 4
For the Project I plan to use Raspberry Pi as I found that a lot of the low-costing thermal cameras out there where compatible with the Raspberry Pi’s so it was an easy choice but As for which raspberry pi I owned 3 types Pi Zero, Pi 3B+ and Pi 4 because the application has a lot of image processing I felt that a pi Zero Just wouldn’t have enough Processing Power. Looking at the remaining I had to take into account the RAM and processing power and the Pi 4 has the 3B+ bet for the task the device will be doing. I think that Pi 4 would be the more suitable option with more processing power and RAM. 

### Adafruit MLX90640 Thermal Camera Breakout
I researched a lot of different thermal cameras and I found that many didn’t have great output as their accuracy was very bad, some being higher than +-10°C which would make huge differences in my device. After a while of searching I found the MLX90640 which has an accuracy of +-2°C which is one of the best I found without going into the premium thermal cameras. I also found documentation on installing the drivers which was an issue I saw a lot of users had when it came to installing certain cameras.

“The MLX90640 contains a 24x32 array of IR thermal sensors. This allows it to return an array of 768 individual infrared temperature readings. It can measure temperatures ranging from -40°C to 300°C with an accuracy of +- 2°C (in the 0-100°C range). With a maximum frame rate of 16 Hz.”(Adafruit MLX90640 IR Thermal Camera, 2021) This is perfect for the application I am making as the range in which I will be looking at is 0-20°C.

<img width="325" alt="Screenshot 2022-03-28 at 13 16 07" src="https://user-images.githubusercontent.com/47002243/160395859-52262c33-bb33-44a4-ac34-43847780e0ee.png">


### Radio Frequency Identification(RFID)
I intend to use a RFID-RC522 board as a way to identify the animal during the process. I will use the reader to get the animal tag number from the cows EID tag that is given to them as a calf. “The tags are activated when they pass within the transmission field of a reader. The tag then absorbs power from the reader and returns its unique 15 digit number back to the reader” (What are EID / RFID Ear Tags, 2022)
As you can see above the code given to the reader is printed on the tag the parts of will be used are the tenth digit to the fifthteeth digit this is the end of the animals tag number. This seems like the most plausible way of identifying each animal efficiently with the full system up and running.

<img width="649" alt="Screenshot 2022-03-28 at 13 14 18" src="https://user-images.githubusercontent.com/47002243/160395564-11aff67a-c323-445a-8001-7b2843d364b5.png">

<img width="369" alt="Screenshot 2022-03-28 at 13 15 20" src="https://user-images.githubusercontent.com/47002243/160395713-4bd14441-592a-4505-acbc-fb8acd00b725.png">
