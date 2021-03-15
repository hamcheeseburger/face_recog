# face_recog pyinstaller 설명서

1. ####spec file 활용하기
    - #####현재 프로젝트에 있는 login_v2.spec에 대한 설명  
    
      pyinstaller는 기본적으로 파이썬 스크립트에서 import한 모듈들을 자동적으로 참조하도록 되어있으나,
      특정 모듈 내에서 import하는 다른 모듈의 경우는 pyinstaller가 찾아내지 못할 때가 있습니다.
      
      제가 실행파일을 만들어 본 결과, pyinstaller가 face_recognition 모듈과 관련한 dat 파일과 h5py 모듈을 찾지 못하는 것을 알아냈습니다.
      **_login_v2.spec_** 파일에서 관련 정보를 Analysis 콜의 *binaries* 옵션과 *hiddenimports* 옵션에 적용한 것을 보실 수 있습니다.
      
      *datas* 옵션에 적용된 파일들은 exe 파일이 *실행될 때 생성되는 실행폴더(_MEIxxxxxx)* 내에 존재하게 됩니다. 이 실행폴더는 프로그램이 종료하면 자동으로 삭제됩니다.  
      즉, exe 파일이 만들어졌을 때 *datas* 옵션에 적용된 파일들은 **<u>exe 파일과 같은 폴더 내에 있지 않아도 정상적으로 프로그램에 적용됩니다.</u>**    
      현재 *datas* 옵션에 적용된 파일들은 아래와 같습니다.
      저는 프로그램에서 사용되는 이미지나, 음성파일 등과 같이 고정적으로 사용되는 파일들을 *datas* 옵션에 적용하였습니다.  
        - 음성안내 파일
        - '카메라 끄기' 버튼을 눌렀을 때 화면에 띄워지는 이미지
        - 자바프로그램
        - 자바프로그램에서 필요한 파일(server.py)
        - TF_best.hdf5 파일
        - negligencedetection 디렉토리
      
      프로그램이 실행되는 도중에 write 해야하는 파일들은 *datas* 옵션에 적용하면 프로그램이 해당 파일을 찾아내지 못합니다.  
      이러한 파일들은 exe 파일과 같은 폴더 내에 존재해야만 정상적으로 실행됩니다.  
      **<u>현재 exe파일과 같은 폴더 내에 존재해야 하는 파일들은 아래와 같습니다.</u>**  
      ![needFolder](./need.png)  
        - CaptureImage 폴더 (빈 폴더만 필요)
        - worklog 폴더 (빈 폴더만 필요)
        - negliencedetection 폴더 (빈 폴더만 필요)
        - data 폴더와 icon 폴더 (내부 항목 모두 필요)
        - python 폴더 (내부 항목 중 client.py 파일만 필요)  
        
      해당 폴더들은 모두 프로젝트내에 존재합니다. 복사하여 사용하시면 됩니다.
      
     **_참조자료_**  
     "spec file 활용법" https://pyinstaller.readthedocs.io/en/stable/spec-files.html   
     "spec file에 face_recognition 관련정보 추가하기" https://github.com/ageitgey/face_recognition/issues/357
    
2. ####spec file로 실행파일 만들기  
    - #####*datas* 옵션에 적용할 파일의 경로 설정  
    
        프로그램이 실행되는 위치에 따라 경로가 달라지게끔 지정을 해주어야 합니다.  
           
        **올바른 방법**  
        <pre><code>
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        MODEL_PATH = scriptDir + os.path.sep + "../model/TF_best.hdf5"
        </code></pre>
      
        **올바르지 않은 방법**  
        <pre><code>
        MODEL_PATH = "../model/TF_best.hdf5"
        </code></pre>
        
   - #####실행파일 만들기  
     
     현재 **login_v2.spec** 파일은 onefile 옵션과 windowed 옵션이 적용되어 있습니다.
     onefile 옵션은 프로그램을 하나의 실행파일로 만들어 줍니다.  
     windowed 옵션은 실행파일 시작 시 콘솔 화면이 같이 실행되지 않게끔 합니다. 
     이에 대한 설정은 spec 파일의 EXE 콜에서 변경 가능 합니다.
     
     설정들을 변경한 후
      <pre><code>
      pyinstaller login_v2.spec
      </code></pre>
     위의 명령어를 터미널에서 실행시킵니다.

     약간의 시간이 흐른 뒤, **dist 폴더** 내에 exe 파일이 생성됩니다.  
     필요한 파일들을 exe 파일과 한 폴더 내에 존재하게 한 후 실행하시면 됩니다.

# 근태관리 프로그램 개요

-----

## 1. 문제의식 & 솔루션 & 기대효과


![image-center]({{ site.url }}{{ site.baseurl }}/README_IMG/2021-03-15 13;53;13.PNG){: .align-center}

