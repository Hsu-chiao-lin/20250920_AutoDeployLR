# 專案任務清單 (To-Do List)

本清單根據 CRISP-DM 流程列出了專案需要完成的所有任務。

---

### 1. 商業理解 (Business Understanding)
- [ ] 與利害關係人進行訪談，確認最終商業目標與評估指標。
- [ ] 盤點所有可用的資料來源與相關欄位。
- [ ] 完成並審閱最終版的專案計畫。

### 2. 資料理解 (Data Understanding)
- [ ] 收集所有需要的原始資料 (e.g., sales data, marketing spend)。
- [ ] 撰寫並執行探索性資料分析 (EDA) 的腳本。
- [ ] 產生資料品質報告，記錄缺失值、異常值的狀況。
- [ ] 繪製變數相關性矩陣圖，初步找出可能影響銷售額的特徵。

### 3. 資料準備 (Data Preparation)
- [ ] 撰寫資料清理腳本。
- [ ] 處理缺失值 (e.g., '促銷活動支出' 補 0)。
- [ ] 進行特徵工程，創建新特徵 (如有需要)。
- [ ] 對類別變數進行 One-Hot 編碼。
- [ ] 將資料集分割為訓練集 (Training Set) 與測試集 (Test Set)。

### 4. 模型建立 (Modeling)
- [ ] 建立多元線性迴歸模型。
- [ ] 建立 Ridge 或 Lasso 迴歸模型以處理共線性問題。
- [ ] 使用交叉驗證 (Cross-Validation) 調整模型超參數。
- [ ] 儲存訓練好的模型 (e.g., using pickle or joblib)。

### 5. 模型評估 (Evaluation)
- [ ] 使用測試集評估模型，計算 R-squared, RMSE, MAE。
- [ ] 繪製殘差圖，分析模型的預測偏差。
- [ ] 撰寫模型評估報告，比較不同模型的表現。

### 6. 部署 (Deployment)
- [ ] 開發 Streamlit Web 應用程式。
- [ ] 設計應用程式的使用者介面 (UI)。
- [ ] 將訓練好的模型載入到 Streamlit 應用中。
- [ ] 撰寫使用者操作手冊。
- [ ] 向利害關係人展示最終成品。

### 專案管理
- [x] 建立 `.gitignore` 檔案。
- [x] 建立 `1_original_project_plan.md`。
- [x] 建立 `2_modified_project_plan.md`。
- [x] 建立 `0_devLog.md`。
- [ ] 建立 `Todo.md`。
- [ ] 建立 `allDone.md`。
