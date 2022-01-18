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

