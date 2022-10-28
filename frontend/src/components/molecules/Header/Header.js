import React from "react";
import PersonIcon from "@mui/icons-material/Person";
import TodayIcon from "@mui/icons-material/Today";
import { IconButton } from "@mui/material";
import "./Header.css";

function Header() {
  return (
    <div className="header">
      <IconButton>
        <PersonIcon className="header__icon" fontSize="large" />
      </IconButton>
      <div className="img">
        <img
          className="header__logo"
          src="https://logos-world.net/wp-content/uploads/2020/09/Tinder-Emblem.png"
          alt="tinder logo"
        />
      </div>
      <IconButton>
        <TodayIcon className="header__icon" fontSize="large" />
      </IconButton>
    </div>
  );
}

export default Header;
