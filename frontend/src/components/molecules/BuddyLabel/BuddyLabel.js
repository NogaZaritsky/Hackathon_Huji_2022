import React from "react";
import { useState } from "react";
import "./BuddyLabel.css";
import pic from "../../../assets/cart-llama-photo.jpg";
import { Avatar } from "@mui/material";
import { display } from "@mui/system";

function BuddyLabel() {
  const [buddy, setBuddy] = useState([
    {
      name: "Achsaf Atzmon",
      img: "/frontend/src/assets/cart-llama-photo.jpg",
      //   ../../../assets/cart-llama-photo.jpg",
    },
    {
      name: "avi asraf",
      img: "/frontend/src/assets/cart-llama-photo.jpg",
      //   ../../../assets/cart-llama-photo.jpg",
    }
  ]);

  return (
    <div className="list-label" key={buddy.name}>
      {buddy.map((user) => (
        <div className="label">
          <p style={{ padding: "10px" }}>{user.name}</p>
          <p>
            <Avatar alt={user.name} src={pic} sx={{ width: 50, height: 50 }} />
          </p>
        </div>
      ))}
    </div>
    //   {/* {data.map(person => (<Card/>))} */}
    //   style={{ backgroundColor: `url(${data.url})` }}
  );
}

export default BuddyLabel;
