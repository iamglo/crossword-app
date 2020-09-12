import axios from 'axios'
const baseUrl = 'http://localhost:8088/api/answer'

const getAll = async () => {
  const request = await axios.get(baseUrl)
  console.log(request.data)
  return request.data
}

const searchKey = async (keyword) => {
  const reformatted = keyword.split(" ").join("+")
  const request = await axios.get(`${baseUrl}/search/${reformatted}`)
  return request.data
}

export default {getAll, searchKey}