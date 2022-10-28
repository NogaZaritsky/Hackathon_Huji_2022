import React from "react";
import {
  Typography,
  AppBar,
  CssBaseline,
  Toolbar,
  Container,
  Grid,
  Fab,
} from "@mui/material";
import PersonIcon from "@mui/icons-material/Person";
import AddIcon from "@mui/icons-material/Add";
import BuddyButton from "../../molecules/BuddyButton/BuddyButton";
import Header from "../../molecules/Header/Header";

const Hero = () => {
  const name = "Achsaf";
  return (
    <div>
      <CssBaseline />
      <Container maxWidth="lg">
        <div>
          <AppBar
            position="relative"
            style={{
              background: "#F74E6A",
              alignItems: "center",
            }}
          >
            <Toolbar>
              <Header />
            </Toolbar>
          </AppBar>
        </div>
      </Container>
    </div>
  );
};

export default Hero;
