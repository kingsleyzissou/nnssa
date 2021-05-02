import React, { useContext, useState, useEffect } from "react";
import classNames from "classnames";
import {
  Button,
  Collapse,
  CustomInput,
  NavbarBrand,
  Navbar,
  NavLink,
  Nav,
  NavItem,
  Container,
  NavbarToggler,
} from "reactstrap";
import { ThemeContext } from '../../contexts/ThemeContext';

/**
 * Custom Navbar component
 * 
 */
export function Navigation() {
  const [collapseOpen, setcollapseOpen] = useState(false);
  const [color, setcolor] = useState("navbar-transparent");
  const { theme, changeTheme } = useContext(ThemeContext);

  const toggleTheme = () => {
    if (theme === '') {
      changeTheme('white-content');
      return;
    }
    changeTheme('');
  };

  useEffect(() => {
    window.addEventListener("resize", updateColor);
    return function cleanup() {
      window.removeEventListener("resize", updateColor);
    };
  });
  const updateColor = () => {
    if (window.innerWidth < 993 && collapseOpen) {
      setcolor("bg-white");
    } else {
      setcolor("navbar-transparent");
    }
  };
  const toggleCollapse = () => {
    if (collapseOpen) {
      setcolor("navbar-transparent");
    } else {
      setcolor("bg-white");
    }
    setcollapseOpen(!collapseOpen);
  };
  return (
    <>
      <Navbar className={classNames("navbar-absolute", color)} expand="lg">
        <Container fluid>
          <div className="navbar-wrapper">
            <NavbarBrand href="/">
              <i className="tim-icons icon-sound-wave" />
              &nbsp;&nbsp;NNSSA
            </NavbarBrand>
          </div>
          <NavbarToggler onClick={toggleCollapse}>
            <span className="navbar-toggler-bar navbar-kebab" />
            <span className="navbar-toggler-bar navbar-kebab" />
            <span className="navbar-toggler-bar navbar-kebab" />
          </NavbarToggler>
          <Collapse navbar isOpen={collapseOpen}>
            <Nav className="ml-auto" navbar>
              <NavItem>
                <NavLink href="https://github.com/kingsleyzissou/nnssa">
                  GitHub
                </NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="http://docs.nnssa.tech">
                  Docs
                </NavLink>
              </NavItem>
              <NavItem>
                <Button color="link">
                  <CustomInput
                    id="switch"
                    type="switch"
                    checked={theme === ''}
                    onChange={toggleTheme}
                  />
                </Button>
              </NavItem>
              <li className="separator d-lg-none" />
            </Nav>
          </Collapse>
        </Container>
      </Navbar>
    </>
  );
}
