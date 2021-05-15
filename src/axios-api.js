import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'https://1qpgrq3olh.execute-api.us-east-2.amazonaws.com/dev'
})

export { getAPI }