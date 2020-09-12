import React, {Component} from 'react';
import {Navbar, Nav} from "react-bootstrap"

const Header = () =>{
  return(
  <Navbar bg="primary" variant="dark">
    <Navbar.Brand href="home">Crossword App</Navbar.Brand>
    <Nav className="mr-auto">
      <Nav.Link href="stats">Stats</Nav.Link>
      <Nav.Link href="sources">Sources</Nav.Link>
      <Nav.Link href="about">About</Nav.Link>
    </Nav>
  </Navbar>
  );
}

export default Header;