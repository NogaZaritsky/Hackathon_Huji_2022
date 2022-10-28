import React from "react";
import { useState } from "react";
import LocationOnIcon from "@mui/icons-material/LocationOn";
import { IconButton } from "@mui/material";

function LocationLabel() {
  const [locData, setData] = useState([
    {
      location: "Infi 2",
      address: "123 Mesilat Yesharim",
    },
  ]);

  return (
    <div className="locLabel" key={locData.subject}>
      {locData.map((loc) => (
        <div>
          <p style={{ padding: "10px" }}>{loc.location}</p>
          <p>{loc.address}</p>
          <IconButton>
            <LocationOnIcon className="header__icon" fontSize="large" />
          </IconButton>
        </div>
      ))}
    </div>
  );
}

export default LocationLabel;
