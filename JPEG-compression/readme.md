THIS HANDS-ON BASED ON [Understanding and Decoding a JPEG Image using Python](https://yasoob.me/posts/understanding-and-writing-jpeg-decoder-in-python).  
You can check origin code in [yasoob/Baseline-JPEG-Decoder](https://github.com/yasoob/Baseline-JPEG-Decoder).

# JPEG 압축과 디코딩 원리

JPEG는 단순히 이미지 포맷일 뿐만 아니라, 압축 알고리즘명이기도 하다.
우리가 접하는 대부분의 JPEG 이미지는 JFIF(JPEG File Interchangable Format) 포맷인데, 이 포맷은 내부적으로 JPEG 압축 알고리즘을 사용한다.

![jpeg_segments](assets/jpeg_segments.png)
from [Ange Albertini](https://twitter.com/angealbertini)  

기본적으로 모든 binary 파일들은 Marker 혹은 Header를 가지는데, 북마크처럼 생각하면 된다.
프로그램이 파일을 읽을때 파일의 어떤 내용이 어느 위치에 저장되어있는지 알려준다.
대부분의 marker는 해당 marker 세그먼트의 length 정보를 들고 있다. 해당 세그먼트가 어느정도 길이인지 알려주는 정보이다.  

`FFD8`과 `FFD9`, `FF01`을 제외하고 나머지 모든 마커는 마커 세그먼트의 길이가 따라붙는다. 
이미지 파일의 시작과 끝은 항상 2바이트 길이다.

## 인코딩 프로세스

![encoding_process](assets/encoding_process.png)
from https://users.cs.cf.ac.uk/Dave.Marshall/Multimedia/node234.html

### JPEG Color Space

[ISO/IEC 10918-6:2013(E), Section 6.1](https://www.itu.int/rec/T-REC-T.872-201206-I/en)에 따르면, JPEG 스펙은 다음과 같다.
- 1개의 컴포넌트로 인코딩된 이미지는 0(black)-255(white)의 grayscale로 간주한다.
- 3개의 컴포넌트로 인코딩된 이미지는 YCbCR로 인코딩된 RGB데이터로 간주한다. 단 이미지가 APP14 마커를 가지고 있는 경우는 마커 데이터에 따라 RGB 혹은 YCbCr 둘 중 하나로 간주 할 수 있다.
- 4개의 컴포넌트로 인코딩된 이미지는 APP14 마커를 가지고 있지 않은 이상 CMYK로 간주한다. APP 14 마커를 가지고 있는 경우는 마커 데이터에 따라 CMYK 혹은 YCCK 둘 중 하나로 간주할 수 있다.

대부분의 JPEG 알고리즘 구현은 RGB 대신 휘도(luminance)와 크로마(chrominance, 동휘도의 참조색과의 색차-color difference-를 의미, YUV 인코딩)를 사용한다.
인간의 눈은 작은 영역의 고주파(high-frequency) 밝기 변화를 잘 감지하지 못하는데, 그래서 주파수를 낮추어 이미지를 압축하더라도 화질에는 별 차이가 없어보이게 된다. JPEG는 이러한 원리를 사용한다.

RGB에서 한 픽셀이 Red, Green, Blue의 3바이트 색상 데이터로 이루어져 있듯, YUV의 한 픽셀도 3바이트로 이루어져있지만 각 바이트가 의미하는 바는 조금 다르다.
Y는 밝기를 결정하는 휘도(luminance, luma), U와 V는 색상을 결정하는 색차(chroma)이다. U는 Blue와의 색차, V는 Red와의 색차를 의미한다.

YUV 포맷은 컬러 텔레비젼이 보편화되지 않았을 때 나왔는데, 기존의 흑백 영상과 컬러 영상을 모두 하나의 포맷으로 처리할 수 있게 호환성을 가지도록 개발되었다.

