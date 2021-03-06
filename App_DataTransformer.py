import streamlit as st


def call_data_transformer():
    st.write(f'Data Transformer called')
    return 'test'


st.set_page_config(layout="wide")
st.title('FER Data Transformer')

buffer_col_width = 1

col_settings, col_buffer = st.columns([2,2])

with col_settings:
    st.header('Settings')
    st.text_input('FER Data Generation Directory',
                  'D:/PhD/My_Databases/FrontalFaces/NewSysTest_6/',
                  )

col_datasets, col_labels, col_process, col_actions, col_status = st.columns([1, 1, 1, 1, 1])

with col_datasets:
    st.header('Select Datasets')

    datasets = [
        'adfes',
        'wsefep',
        'jaffe',
        'impa',
        'tfeid',
        'ckext',
        'kdef'
    ]

    datasets_selected = {}
    for i, dataset in enumerate(datasets):
        datasets_selected[i] = st.checkbox(dataset.upper(), value=True)

with col_labels:
    st.header('Select Labels')
    labels = [
        'Neutral',
        'Anger',
        'Disgust',
        'Fear',
        'Joy',
        'Sadness',
        'Surprise',
        'Contempt',
        'Embarrassment',
        'Pride'
    ]

    labels_selected = {}
    for i, label in enumerate(labels):
        labels_selected[i] = st.checkbox(label.title(), value=i < 7)

with col_process:
    st.header('Process Options')
    flip_image = st.checkbox('Flip image', value=True)
    align_faces = st.checkbox('Align faces', value=True)
    hist_eq = st.checkbox('Histogram EQ', value=False)
    generate_images = st.checkbox('Generate images', value=False)

    image_size = st.text_input('Image size', value=224)

    color_option = st.selectbox(
        'Output image color',
        ('Grayscale', 'RGB')
    )

with col_actions:
    st.header('Transform Data')
    if st.button("Process faces"):
        result = call_data_transformer()
        st.write(color_option)

with col_status:
    st.header('Log')
    st.info('Processing ADFES dataset')
    st.progress(1.0)
    st.info('Processing CKEXT dataset')
    st.progress(0.67)