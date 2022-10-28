import React from "react";
import { Button } from "@material-ui/core";
import { withStyles } from "@material-ui/core/styles";

const StyledButton = withStyles({
  root: {
    margin: "auto",
    display: "flex",
    alignItems: "center",
    justifyContent: "space-around",
    height: "60px",
    padding: "10",
    boxSizing: "border-box",
    width: "250px",
    borderRadius: 10.5,
    background: "#F74E6A",
    fontSize: "20px",
    fontWeight: "bold",
    color: "#F4DEE7",
    transform: "none",
    textTransform: "capitalize",
    marginBottom: "8px",
    transition: "background .3s,border-color .3s,color .3s",
    "&:hover": {
      backgroundColor: "#F86459",
    },
  },
  label: {
    textTransform: "capitalize",
  },
})(Button);

export default function CustomButton(props) {
  return (
    <StyledButton variant="contained" onClick={props.action}>
      {props.avatar}
      <div>{props.txt}</div>
    </StyledButton>
  );
}
