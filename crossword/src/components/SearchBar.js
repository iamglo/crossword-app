import React, {useState, Component} from 'react';
import { Form, Button, Col } from 'react-bootstrap'
import clueService from '../services/clues'
import answerService from '../services/answers'

const SearchBar = ({changeState}) => {
  const [answer, setAnswer] = useState("")
  const [clue, setClue] = useState("")

  const handleClueSubmit = (e) => {
    e.preventDefault();
    
    if (clue == ""){
      clueService.getAll()
      .then((res) => {
        changeState(res)
      })
      .catch(console.log)
    }
    else{
      clueService.searchKey(clue)
      .then((res) => {
        changeState(res)
      })
      .catch(console.log)
    }
  }

  const handleAnswerSubmit = (e) => {
    e.preventDefault();

    if (answer === "") {
      clueService.getAll()
      .then((res) => {
        changeState(res)
      })
      .catch(console.log)
    }
    else {
      answerService.searchKey(answer)
      .then((res) => {
        changeState(res)
      })
      .catch(console.log)
    }
  }

  const handleChange = (e) => {
    const target = e.target;
    const value = target.value
    const name = target.name
    if (name === 'clue'){
      setClue(value)
    }
    else if (name == 'answer'){
      setAnswer(value)
    } 
  }

  return (
    <div>
    <Form id="searchForm" onSubmit={handleAnswerSubmit} >
      <Form.Row className="align-items-center">
        <Col sm={3} className="my-1">  
            <Form.Label>Search by Answer  </Form.Label>
        </Col>
        <Col sm={5} className="my-1">  
            <Form.Control name='answer' type="answer" placeholder="Search Answer" onChange={handleChange} />
        </Col>
        <Col xs="auto" className="my-1">
          <Button type="submit">
            Load
          </Button>
        </Col>
      </Form.Row>
    </Form>
       <Form id="searchForm" onSubmit={handleClueSubmit} >
       <Form.Row className="align-items-center">
         <Col sm={3} className="my-1">  
             <Form.Label>Search by Clue </Form.Label>
         </Col>
         <Col sm={5} className="my-1">  
             <Form.Control name='clue' type="clue" placeholder="Search Clue" onChange={handleChange} />
         </Col>
         <Col xs="auto" className="my-1">
           <Button type="submit">
             Load
           </Button>
         </Col>
       </Form.Row>
     </Form>
    </div> 
  )
}

export default SearchBar