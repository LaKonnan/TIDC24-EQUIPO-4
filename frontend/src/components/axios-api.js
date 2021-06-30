import axios from 'axios'

const getAPI = axios.create({
   // baseURL: 'https://ee7rryknn1.execute-api.us-east-2.amazonaws.com/dev'
    baseURL: 'http://localhost:5000'
})

export { getAPI }