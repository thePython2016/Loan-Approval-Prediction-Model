import pickle as pkl
import  pandas as pd
import streamlit as st

model=pkl.load(open("model.pkl","rb"))
labelEncoder=pkl.load(open("labelEncoder.pkl","rb"))

st.title("Loan Approval Prediction App")

tab1,tab2=st.tabs(["Load Application Form","Loan Application Upload Form"])

with tab1:

    st.markdown("""
        <style>
        .error-box {
            background-color: #fff0f0;
            border-left: 4px solid #ff4b4b;
            border-radius: 4px;
            padding: 8px 12px;
            margin-bottom: 10px;
            color: #cc0000;
            font-size: 14px;
        }
        /* Style the dismiss button to look like an X */
        div[data-testid="stButton"] button[kind="secondary"]#dismiss-btn {
            position: absolute;
            top: 8px;
            right: 12px;
            background: none;
            border: none;
            font-size: 18px;
            cursor: pointer;
            opacity: 0.6;
            padding: 0;
            min-height: unset;
            height: auto;
            width: auto;
            color: inherit;
        }
        div[data-testid="stButton"] button[kind="secondary"]#dismiss-btn:hover {
            opacity: 1;
        }
        .result-wrapper {
            position: relative;
            margin-bottom: 16px;
        }
        .result-box {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 40px 12px 16px;
            border-radius: 6px;
            font-size: 15px;
            font-weight: 500;
        }
        .result-approved {
            background-color: #f0fff4;
            border-left: 4px solid #28a745;
            color: #155724;
        }
        .result-rejected {
            background-color: #fff0f0;
            border-left: 4px solid #ff4b4b;
            color: #cc0000;
        }
        </style>
    """, unsafe_allow_html=True)

    # ── Manage dismiss state ───────────────────────
    if "show_result" not in st.session_state:
        st.session_state.show_result = False
    if "result_label" not in st.session_state:
        st.session_state.result_label = ""
    if "result_approved" not in st.session_state:
        st.session_state.result_approved = False

    # ── Result + Dismiss at the TOP ───────────────
    if st.session_state.show_result:
        css_class = "result-approved" if st.session_state.result_approved else "result-rejected"
        icon      = "✅" if st.session_state.result_approved else "❌"
        label     = st.session_state.result_label

        col1, col2 = st.columns([11, 1])
        with col1:
            st.markdown(f"""
                <div class="result-box {css_class}">
                    {icon} &nbsp; Loan Status: <strong>{label}</strong>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("✕", key="dismiss_result"):
                st.session_state.show_result = False
                st.rerun()

    # ── Number of Dependents ──────────────────────
    errorDependent = st.empty()
    numberDependent = st.number_input("Number of Dependents", min_value=0)

    # ── Education ────────────────────────────────
    errorEducation = st.empty()
    education = st.selectbox("Education", ["Select Education Level", "Graduate", "Not Graduate"])

    # ── Employment ───────────────────────────────
    errorEmployment = st.empty()
    Employment = st.selectbox("Employment Status", ["Select Employment Status", "Yes", "No"])

    # ── Annual Income ────────────────────────────
    errorIncome = st.empty()
    AnnualIncome = st.number_input("Annual Income", min_value=0)

    # ── Loan Amount ──────────────────────────────
    errorLoan = st.empty()
    loanAmount = st.number_input("Loan Amount", min_value=0)

    # ── Residential Asset Value ──────────────────
    errorResidential = st.empty()
    residentialAssetValue = st.number_input("Residential Asset Value", min_value=0)

    # ── Commercial Asset Value ───────────────────
    errorCommercial = st.empty()
    commercialAssetvalue = st.number_input("Commercial Asset Value", min_value=0)

    # ── Luxury Asset Value ───────────────────────
    errorLuxury = st.empty()
    luxuryAssetValue = st.number_input("Luxury Asset Value", min_value=0)

    # ── Bank Asset Value ─────────────────────────
    errorBank = st.empty()
    bankAssetValue = st.number_input("Bank Asset Value", min_value=0)

    button = st.button("Predict")

    def showError(placeholder, msg):
        placeholder.markdown(f"""
            <div class="error-box">⚠️ {msg}</div>
        """, unsafe_allow_html=True)

    def clearAll():
        errorDependent.empty()
        errorEducation.empty()
        errorEmployment.empty()
        errorIncome.empty()
        errorLoan.empty()
        errorResidential.empty()
        errorCommercial.empty()
        errorLuxury.empty()
        errorBank.empty()

    if button:
        clearAll()
        st.session_state.show_result = False

        if numberDependent <= 0:
            showError(errorDependent, "Enter Number of Dependents")
        elif education == "Select Education Level":
            showError(errorEducation, "Please Select Education Level")
        elif Employment == "Select Employment Status":
            showError(errorEmployment, "Please Select Employment Status")
        elif AnnualIncome <= 0:
            showError(errorIncome, "Enter Annual Income")
        elif loanAmount <= 0:
            showError(errorLoan, "Enter Loan Amount")
        elif residentialAssetValue <= 0:
            showError(errorResidential, "Enter Residential Asset Value")
        elif commercialAssetvalue <= 0:
            showError(errorCommercial, "Enter Commercial Asset Value")
        elif luxuryAssetValue <= 0:
            showError(errorLuxury, "Enter Luxury Asset Value")
        elif bankAssetValue <= 0:
            showError(errorBank, "Enter Bank Asset Value")
        else:
            data = pd.DataFrame({
                "noofdependents":         [numberDependent],
                "education":              [education],
                "selfemployed":           [Employment],
                "incomeannum":            [AnnualIncome],
                "loanamount":             [loanAmount],
                "residentialassetsvalue": [residentialAssetValue],
                "commercialassetsvalue":  [commercialAssetvalue],
                "luxuryassetsvalue":      [luxuryAssetValue],
                "bankassetvalue":         [bankAssetValue]
            })
            data.columns = data.columns.str.strip().str.replace(" ", "").str.replace("_", "")
            data.columns = data.columns.str[0].str.lower() + data.columns.str[1:]

            for records in data.columns:
                if data[records].dtype not in ['int64', 'float64']:
                    data[records] = data[records].str.strip()

            # Encode
            data['education']    = data['education'].map({"Graduate": 1, "Not Graduate": 0})
            data['selfemployed'] = data['selfemployed'].map({"Yes": 1, "No": 0})

            # Predict
            prediction = model.predict(data)
            result     = labelEncoder.inverse_transform(prediction)

            # ── Store result in session state ──────
            st.session_state.show_result    = True
            st.session_state.result_label   = result[0]
            st.session_state.result_approved = (result[0] == "Approved")
            st.rerun()
with tab2:
    st.markdown("""
        <style>
            /* Hide default streamlit uploader and restyle */
            [data-testid="stFileUploader"] {
                border: 2px dashed #cccccc !important;
                border-radius: 12px !important;
                padding: 40px 20px !important;
                text-align: center !important;
                background-color: #fafafa !important;
            }
            [data-testid="stFileUploader"]:hover {
                border-color: #ff4b4b !important;
                background-color: #fff5f5 !important;
            }
            [data-testid="stFileDropzoneInstructions"] {
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
            }
            [data-testid="stFileUploaderDropzoneInstructions"] svg {
                width: 48px !important;
                height: 48px !important;
                color: #888 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #333;
            margin-bottom: 16px;
        ">Upload Loan Application File</div>
        <div style="
            text-align: center;
            font-size: 14px;
            color: #888;
            margin-bottom: 20px;
        ">Upload a CSV file to predict loan approval for multiple applications</div>
    """, unsafe_allow_html=True)

    fileData   = st.file_uploader("Select a CSV file to upload", type="csv", label_visibility="collapsed")
    buttonFile = st.button("Predict Loan", use_container_width=True)

    if buttonFile:
        if not fileData:
            st.markdown("""
                <div style="
                    background-color: #fff0f0;
                    border-left: 4px solid #ff4b4b;
                    border-radius: 4px;
                    padding: 10px 14px;
                    color: #cc0000;
                    font-size: 14px;
                    margin-top: 10px;
                ">⚠️ Please upload a CSV file before predicting</div>
            """, unsafe_allow_html=True)
        else:
            file = pd.read_csv(fileData)
            file.columns = file.columns.str.strip().str.replace(" ", "").str.replace("_", "")
            file.columns = file.columns.str[0].str.lower() + file.columns.str[1:]

            for records in file.columns:
                if file[records].dtype not in ['int64', 'float64']:
                    file[records] = file[records].str.strip()

            file['education']    = file['education'].map({"Graduate": 1, "Not Graduate": 0})
            file['selfemployed'] = file['selfemployed'].map({"Yes": 1, "No": 0})

            filePrediction = model.predict(file)
            resultFile     = labelEncoder.inverse_transform(filePrediction)
            file["Predicted Loan Application"] = resultFile

            # Summary counts
            approved = (resultFile == "Approved").sum()
            rejected = (resultFile == "Rejected").sum()

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                    <div style="
                        background-color: #f0fff4;
                        border-left: 4px solid #28a745;
                        border-radius: 8px;
                        padding: 16px;
                        text-align: center;
                        font-size: 18px;
                        font-weight: bold;
                        color: #155724;
                    ">✅ Approved<br>{approved}</div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                    <div style="
                        background-color: #fff0f0;
                        border-left: 4px solid #ff4b4b;
                        border-radius: 8px;
                        padding: 16px;
                        text-align: center;
                        font-size: 18px;
                        font-weight: bold;
                        color: #cc0000;
                    ">❌ Rejected<br>{rejected}</div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Highlight rows
            def highlightResult(row):
                if row['Predicted Loan Application'] == 'Approved':
                    return ['background-color: #d4edda'] * len(row)
                else:
                    return ['background-color: #f8d7da'] * len(row)

            st.dataframe(file.style.apply(highlightResult, axis=1))