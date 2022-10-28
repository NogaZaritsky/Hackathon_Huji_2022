import React from "react";
import {
  Typography,
  Avatar,
  AppBar,
  Card,
  CssBaseline,
  GridTypeMap,
  Toolbar,
  Container,
  Grid,
  Box,
  Button,
} from "@mui/material";
import PersonIcon from "@mui/icons-material/Person";
import { useState } from "react";
import pic from "../../../assets/cart-llama-photo.jpg";
import { styled } from "@mui/system";
import { Stack } from "@mui/material";
import Paper from "@mui/material/Paper";
import CustomButton from "../../atoms/CustomButton/CustomButton";

function BuddyButton() {
  const [buddy, setBuddy] = useState([
    {
      name: "Achsaf Atzmon",
      img: "/frontend/src/assets/cart-llama-photo.jpg",
    },
    {
      name: "Achsaf Atzmon",
      img: "/frontend/src/assets/cart-llama-photo.jpg",
    },
  ]);
  return (
    <div>
      <CssBaseline />
      <div>
        <Box sx={{ width: "100%" }}>
          {buddy.map((user) => (
            <CustomButton
              txt={user.name}
              avatar={
                <Avatar
                  alt={user.name}
                  src={pic}
                  sx={{ width: 50, height: 50 }}
                />
              }
            ></CustomButton>
          ))}
        </Box>
      </div>
    </div>
  );
}

export default BuddyButton;
