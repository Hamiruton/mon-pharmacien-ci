import axios from "axios";

const axiosPlugin = {
    install(app) {
        const axiosInstance = axios.create({
            baseURL: 'http://localhost:8000/api',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            }
        });

        axiosInstance.interceptors.response.use (
            function(response) {
                return response
            },
            function(error) {
                alert(error.response ? error.response.data.error : error.message);
                return Promise.resolve(error);
            }
        );

        app.provide('axios', axiosInstance);
        app.config.globalProperties.$axios = axiosInstance;
    },
};

export default axiosPlugin;