import { useState, useEffect } from "react";
import React, {Component} from "react"
import "./App.css";
import Home from "./views/Home";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { red } from "@mui/material/colors";
import Hero from "./components/organisms/Hero/Hero";
import SignUp from "./components/organisms/SignUp/SignUp";

const PAGES = {
  HOME: "home",
  SIGNUP: "signup",
};

const theme = createTheme({
  palette: {
    primary: {
      main: red[500],
    },
    typography: {
      fontFamily: [
        "-apple-system",
        "BlinkMacSystemFont",
        '"Segoe UI"',
        "Roboto",
        '"Helvetica Neue"',
        "Arial",
        "sans-serif",
        '"Apple Color Emoji"',
        '"Segoe UI Emoji"',
        '"Segoe UI Symbol"',
      ].join(","),
    },
  },
});

function App() {
  const [currentPage, setCurrentPage] = useState(PAGES.HOME);
  const ToRender = Home;

  //   // Receive Data
  //   useEffect(() => {
  //     async function fetchData() {
  //       try {
  //         const res = await axios.get('http://127.0.0.1:8000/customer/');
  //         console.log(res)
  //         const table = await res.data;
  //         console.log(table);
  //       }
  //       catch (e){
  //         console.log(e);
  //       }
  //     }
  //     fetchData()
  //   });
  //   // Send Data
  //   useEffect(() => {
  //     async function fetchData() {
  //       try {
  //         axios.get('http://127.0.0.1:8000/make_match/?want_match=4')
  //         .then((response) => {
  //           console.log(response);
  //         }, (error) => {
  //           console.log(error);
  //         });
  //         console.log("HERE\n");
  //       }
  //       catch (e){
  //         console.log(e);   
  //       }
  //     }   
  //     fetchData()
  // });
  //       <Hero />


  const changeView = () => {
    console.log("change page");
    setCurrentPage(PAGES.SIGNUP);
  };

  return (
    
    <div className="App">

      {/* <Hero /> */}
      <SignUp />
      <ToRender />
      {/* {currentPage == PAGES.HOME ? <Home /> : <></>} */}
      {/* {switch (openPage)} */}
      {/* do here an if else */}
      

      <Hero />
      {currentPage == PAGES.HOME ? <Home action={changeView} /> : <SignUp />}
    </div>
    
  );
}

export default App;
