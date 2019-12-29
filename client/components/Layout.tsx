import "bootstrap/dist/css/bootstrap.min.css";
import Head from "next/head";
import * as React from "react";
import { useState } from "react";
import {
    Collapse,
    Container,
    Nav,
    Navbar,
    NavbarBrand,
    NavbarToggler,
    NavItem,
    NavLink,
} from "reactstrap";

type Props = {
    title?: string
}

const Layout: React.FunctionComponent<Props> = ({
    children,
    title = "This is the default title",
}) => {
    const [isOpen, setIsOpen] = useState(false);

    const toggle = () => setIsOpen(!isOpen);

    return (
      <Container>
          <Head>
              <title>{title}</title>
              <meta charSet="utf-8" />
              <meta
                name="viewport"
                content="initial-scale=1.0, width=device-width"
              />

          </Head>
          <Navbar color="light" light className="m-3" expand="md">
              <NavbarBrand>
                  Verbum: <small><i>Upload snippets, find similar sentences</i></small>
              </NavbarBrand>
              <NavbarToggler onClick={toggle} />
              <Collapse isOpen={isOpen} navbar className="float-right">
                  <Nav className="mr-auto" navbar>
                      <NavItem>
                          <NavLink href="/">Home</NavLink>
                      </NavItem>
                      <NavItem>
                          <NavLink href="/upload">Upload</NavLink>
                      </NavItem>
                  </Nav>
              </Collapse>
          </Navbar>
          <Container className="themed-container">
              {children}
          </Container>
      </Container>
    );
};

export default Layout;
