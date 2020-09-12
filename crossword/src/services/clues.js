import axios from 'axios'
const baseUrl = 'http://localhost:8088/api/clue'

const getAll = async () => {
  const request = await axios.get(`${baseUrl}/all`)
  return request.data
}

const get = async (search) => {
  let add_on = ``
  for (var key in search){
    add_on += `${key}=${search[key]}&`
  }
  const request = await axios.get(`${baseUrl}?${add_on}`)
  return request.data
}

const searchKey = async (keyword) => {
  const reformatted = keyword.split(" ").join("+")
  const request = await axios.get(`${baseUrl}/search/${reformatted}`)
  return request.data
}

export default {getAll, get, searchKey}