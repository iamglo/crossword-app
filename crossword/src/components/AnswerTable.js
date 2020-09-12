import React from 'react'
import {MDBDataTableV5 } from 'mdbreact'
import moment from 'moment'

const AnswerTable = ({data}) => {
  const renderTable = (obj) => {
    if (obj && obj.length > 0){
      if ('clue_id' in obj[0]){
        const mapper = obj.map((c, index) => {
          const {answer, clue, clue_id, date, day_of_week, source} = c
          let format_date = `${date.slice(0, -6)}/${date.slice(-6,-4)}/${date.slice(-4)}`
          // let reformat_date = moment(test).format('MM/DD/YYYY')
          
          return(
            {
              answer: answer[0].answer,
              clue: clue,
              date: format_date,
              source: source
            })
        })
        // console.log(mapper)
        return mapper
      }
      else{
        const mapper = obj.map((c, index) => {
          const {answer, clue} = c
          return clue.map((m, index) => {
            const {clue, date, day_of_week, source} = m
            let format_date = `${date.slice(0, -6)}/${date.slice(-6,-4)}/${date.slice(-4)}`
            return(
              {
                answer: answer,
                clue: clue,
                date: format_date,
                source: source
              })
          })})

        // console.log(mapper)
        return mapper.flat(1) }
      }
    }


  const data_obj = {
    columns:[
      {
        label: 'Clue',
        field: 'clue',
        width: 100, 
        attributes: {
          'aria-controls': 'DataTable',
          'aria-label': 'Name',
        },
      },
      {
        label: 'Answer',
        field: 'answer',
        sort: 'asc',
        width: 50
      },
      {
        label: 'Date',
        field: 'date',
        sort: 'asc',
        width: 50
      },
      {
        label: 'Source',
        field: 'source',
        sort: 'asc',
        width: 50
      }
    ],
    rows: renderTable(data)
  }

  return (
    <div>
      <MDBDataTableV5  
        entries={25}
        bordered
        small
        pagingTop
        searchTop 
        searchBottom={false} 
        data={data_obj}
        barReverse
      />
    </div>
  )
}

export default AnswerTable