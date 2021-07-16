# **YOLO.V3 and YOLO.v5**

# **In real time using Flask**

**Install dependencies:**

- **python -m venv venv**
- **venv\Scripts\activate**
- **python -m pip install -r requirements.txt**

**Change the Source as per your choice (in web.py):**

- ![](RackMultipart20210716-4-9gv36p_html_5f74e973e5f1bf6b.png)

**This is for v3. Change the value of source to the rtsp/rtmp/https url (make sure they are in single quotes)**

- ![](RackMultipart20210716-4-9gv36p_html_f9eb050b6b121b93.png)

**This is for v5. Enter you rtsp/rtmp/https url in place of \&lt;your rtsp yrl\&gt; in the argument section of the function yolo.run()**

**This repository has a both the YOLO.V3 and the YOLO.V5 in it.**

- **YOLO.V3: it is present in the actual folder. To execute it, run this in the terminal/powershell:**
  - **venv\Scripts\activate**
  - **python web.py**
- **YOLO.V5: it is present in the yolloFlask subfolder. To execute yolo v5, run this in the terminal/powershell:**
  - **cd yoloflask**
  - **venv\Scripts\activate**
  - **python web.py**
