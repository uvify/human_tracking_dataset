<!-- #Title -->
# drone_tracking_dataset

## Human tracking dataset captured by drone.


<p align='center'>
    <img src="./config/doc/example1.png" alt="drawing" width="400" />
    <img src="./config/doc/example2.png" alt="drawing" width="400" />
</p>


## Dataset Download 


- [Train set ](http://www.naver.com)
(Train set images extracted with 3fps)
- [Test set](http://www.google.com)
(Test set images extracted with 3fps)

## Directory Structure
<pre>
 [root path]/
 └──[test or train]/                  
    └──[(sequence number)_seqence]/
       ├──(sequence_number).txt     <--- ground truth
       └──[images]/
          └──(frame_number).png     <--- image
</pre>


## How to run? 

### 1. Dataset Viewer

``` ruby
 python3 visualize_data.py --dir=[root_dir_path] --type=[train or test] --seq=[sequence number( 450 <= test < 500 ,  0 <= train < 450)]
```

<pre>
key 'q' 'esc' : exit program
key 'n' '->'  : next frame
key 'p' '<-'  : prev frame
</pre>


### 2. Evaluation
> TBD


## Data Distribution

|type  |total |  train  |  test |
|:-----|:------:|:------:|------:|
|# img |18000   |13500   | 4500  |

|degree |total |  general  | top view |
|:-----|:------:|:------:|------:|
|# img  |18000 |14370   |3630   |

|weather |total | sunny  | cloudy |
|:-----|:------:|:------:|------:|
|# img |18000 |10320   |7680   |

|space |total | general  | green | play |
|:-----|:------:|:------:|------:| ------:|
|# img |18000|10320   |7680   |  2100  |

<p align='center'>
    <img src="./config/doc/data_ratio.png" alt="drawing" width= "200"/>
    <img src="./config/doc/degree.png" alt="drawing" width= "200"/>
    <img src="./config/doc/weather_ratio.png" alt="drawing" width= "200"/>
    <img src="./config/doc/space_ratio.png" alt="drawing" width= "200"/>    
</p>



## Class Distribution
|      | total  |  general-pose | sitting  | waving hand|
|:-----|:------:|------:|------:|------:|
|# obj    | 144448  | 134413  | 9535|500|

|      | total | occluded  | not occluded |
|:-----|:------:| :------:|------:|
|# obj    | 144448 |49593   | 94855|

|      | total | truncated  | not truncated |
|:-----|:------:| :------:|------:|
|# obj | 144448 | 10487   | 133961|


<p align='center'>
    <img src="./config/doc/pose_distribution.png" alt="drawing" width= "250"/>
    <img src="./config/doc/occlusion.png" alt="drawing" width = "250"/>
    <img src="./config/doc/truncation.png" alt="drawing" width= "250"/>
</p>





## Example Data
<p align='center'>
    <img src="./config/doc/top_example.png" alt="drawing" width="400" />
    <img src="./config/doc/general_example.png" alt="drawing" width="400" />
</p>

<p align='center'>
    <img src="./config/doc/example3.png" alt="drawing" width="400" />
    <img src="./config/doc/example4.png" alt="drawing" width="400" />
</p>

