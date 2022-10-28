import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import CheckboxList from "../../atoms/CheckboxList/CheckboxList";
import axios from 'axios';

async function fetchData() {
        try {
          axios.get('http://127.0.0.1:8000/make_match/?want_match=2')
          .then((response) => {
            console.log(response);
          }, (error) => {
            console.log(error);
          });
          console.log("HERE\n");
        }
        catch (e){
          console.log(e);   
        }
      };

const courses = [
  {
    number: "67315",
    name: "CC++",
  },
  {
    number: "80132",
    name: "Calculus 2",
  },
  {
    number: "80135",
    name: "Linear Algebra 2",
  },
  {
    number: "67109",
    name: "Data Structures",
  },
];
const theme = createTheme();

export default function SignUp() {
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get("email"),
      password: data.get("password"),
    });
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="sm">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Typography
            component="h1"
            variant="h5"
            fontFamily={"Montserrat"}
            fontWeight="700"
          >
            Let's Study
          </Typography>
          <Box
            component="form"
            noValidate
            onSubmit={handleSubmit}
            sx={{ mt: 3 }}
          >
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <CheckboxList props={courses} />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="studyPlan"
                  label="What would you like to study?"
                  name="studyPlan"
                  autoComplete="study-plan"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete="date"
                  name="date"
                  required
                  fullWidth
                  id="date"
                  label="Date"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete="time"
                  name="time"
                  required
                  fullWidth
                  id="time"
                  label="Time"
                  autoFocus
                />
              </Grid>
            </Grid>
            <Grid item xs={12} sm={6}>
              <Button
                type="submit"
                fullWidth
                variant="contained"
                style={{ backgroundColor: "#F86459" }}
                sx={{ mt: 3, mb: 2 }} onClick = {fetchData} >
                Sign Up
              </Button>
            </Grid>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
