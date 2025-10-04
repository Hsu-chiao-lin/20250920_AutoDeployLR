# 如何將專案部署到 Replit

Replit 是一個免費的線上 IDE，非常適合用來快速部署像 Streamlit 這樣的 Web 應用程式。以下是將本專案部署到 Replit 的詳細步驟。

### 步驟 1：建立 Replit 專案

1.  前往 [Replit](https://replit.com/) 並登入您的帳號。
2.  點擊左上角的 **+ Create Repl** 按鈕。
3.  在範本 (Template) 搜尋框中輸入 `Python` 並選取它。
4.  為您的專案取一個標題 (Title)，然後點擊 **+ Create Repl**。

### 步驟 2：上傳專案檔案

專案建立後，您會看到一個檔案列表、一個編輯器和一個 Shell (終端機) 視窗。

1.  在左側的檔案列表 (Files) 區域，點擊右上角的三個點 (⋮) 圖示。
2.  選擇 **Upload folder**，然後選擇您電腦上的整個專案資料夾，將所有檔案一次性上傳。
3.  或者，您也可以選擇 **Upload file**，逐一上傳以下所有檔案：
    - `app.py`
    - `requirements.txt`
    - `.gitignore`
    - `README.md`
    - `0_devLog.md`
    - `1_original_project_plan.md`
    - `2_modified_project_plan.md`
    - `Todo.md`
    - `allDone.md`

### 步驟 3：安裝 Python 套件

Replit 通常會自動偵測 `requirements.txt` 並安裝套件。如果沒有自動安裝，您可以在右側的 **Shell** 視窗中手動執行以下指令：

```bash
pip install -r requirements.txt
```

等待所有套件（streamlit, numpy, pandas 等）安裝完成。

### 步驟 4：設定執行指令

為了讓 Replit 知道如何執行 Streamlit 應用程式，我們需要修改它的執行設定。

1.  在左側的檔案列表中，找到並點擊 `.replit` 這個設定檔。
2.  將檔案內容修改如下：

    ```toml
    # .replit
    entrypoint = "app.py"
    
    [run]
    command = "streamlit run app.py --server.address 0.0.0.0 --server.port $PORT"
    ```

    **說明：**
    - `entrypoint`: 指定主要的執行檔案。
    - `command`: 這是最重要的部分。它告訴 Replit 在點擊 "Run" 按鈕時，要執行 `streamlit run` 指令，並將其綁定到 Replit 的網路環境中。

### 步驟 5：執行與查看應用程式

1.  完成以上設定後，點擊畫面最上方的綠色 **Run** 按鈕。
2.  程式開始執行後，畫面右側會出現一個 **Webview** 視窗，您的 Streamlit 應用程式將會顯示在這裡。
3.  您可以直接在 Webview 中與應用程式互動，就像在本地電腦上一樣。

恭喜！您已成功將 Streamlit 應用程式部署到 Replit。
