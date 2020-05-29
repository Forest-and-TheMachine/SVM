# SVM
installation while pip method is too slow 
=========================================

a useful website: https://www.lfd.uci.edu/~gohlke/pythonlibs 

install cvxopt
--------------
step1:<br>
    1). Use pip version 19.2 or newer to install the downloaded .whl files.<br>
    2). Install numpy+mkl before other packages that depend on it.<br>
        https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy<br><br>
        e.g. numpy-1.16.6mkl-cp36-cp36m-win_amd64.whl, with respect to python3.6, "-cp36" means python3.6, "-cp37" means python3.7 ...<br>
        `NOTE`: maybe it is still too slow to download this .whl file. Search on the https://download.csdn.net/ with right name.<br>
    3). choose a proper version on the website below:<br>
        https://www.lfd.uci.edu/~gohlke/pythonlibs/#cvxopt<br>
        e.g. cvxpy-1.0.31-cp36-cp36m-win_amd64.whl, with respect to python3.6, "-cp36" means python3.6, "-cp37" means python3.7 ...<br>
        this .whl file is less than 1M, u can download it directly.<br>
step2: <br>
    1). In a cmd line go to the folder where u put the downloaded .whl files.<br>
        e.g. C:\Users\fredy>cd C:\Users\fredy\Downloads<br>
    2). pip install numpy-1.16.6mkl-cp36-cp36m-win_amd64.whl<br>
    3). pip install cvxpy-1.0.31-cp36-cp36m-win_amd64.whl<br>
    
    
ImportError: 
------------
DLL load failed: The specified module could not be found.<br>
Solution: prepending `path` with the directory containing `mkl_rt.ddl`<br>
Reference: https://github.com/cvxopt/cvxopt/issues/127

step1: <br>
    1). find the directory path<br>
    ![i found it on pycharm](https://github.com/Forest-and-TheMachine/SVM/blob/master/1.png)<br>
    ![mkl_rt.ddl](https://github.com/Forest-and-TheMachine/SVM/blob/master/2.jpg)<br>
    
    2). Open the `System Properties` window(win+r, input sysdm.cpl) and click on the `Adanced` tab.<br>
        Click the `Environment Variables` button at the bottom.<br> 
        In the `User variables section`, select `Path` and click `Edit`. <br>
        Add the directory that contains `mkl_rt.dll` to the path. <br>
        You will probably need to restart Python after updating the path.<br>





