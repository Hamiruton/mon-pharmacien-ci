import axios from 'axios';


export async function uploadFile(file, idPatient, bon_assurance, userToken) {
  const config = {
    baseURL: 'http://localhost:8000/api',
    headers: {
      Authorization: 'Bearer ' + userToken,
      'Content-Type': 'multipart/form-data',
    },
  };

  const formData = new FormData();
  formData.append('file', file);
  formData.append('id_patient', idPatient);
  formData.append('bon_assurance', bon_assurance);

  let filepath = null;

  try {
    const response = await axios.post('/client/upload', formData, config);

    if (response.status === 201 /*&& response.data.message.length > 0*/) {
      filepath = response.data.path;
    }
  } catch (error) {
    alert(error.response ? error.response.data.error : error.message);
  }

  return filepath;
}


export function formatDate(dateString, inputField = false) {
  if (!dateString) return '';

  let formattedDate = new Date(dateString).toLocaleDateString('fr-FR');

  if (inputField){
    formattedDate = formattedDate.split('/').reverse().join('-');
  }

  return formattedDate;
}