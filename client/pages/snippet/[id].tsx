import axios from "axios";
import { NextPage } from "next";
import Error from "next/error";
import * as React from "react";
import { Col, Row } from "reactstrap";
import Layout from "../../components/Layout";
import SentenceList from "../../components/SentenceList";

interface Props {
    snippet?: FullSnippet;
}

const Snippet: NextPage<Props> = ({ snippet }) => {
    if (!snippet) {
        return <Error statusCode={404} />;
    }
    return (
      <Layout title={`Verbum : Snippet ${snippet?.id}`}>
          <Row className="mb-3 text-center">
              <Col>
                  <h3>Snippet id: {snippet?.id} with {snippet?.count} sentences</h3>
              </Col>
          </Row>
          <SentenceList sentences={snippet?.parts} />
      </Layout>
    );
};

Snippet.getInitialProps = async ({ query, res }) => {
    const id = query.id;
    const snippet = await axios
      .get<FullSnippet>(`http://localhost:5000/snippets/${id}`)
      .then(d => d.data);
    if (!snippet && res) {
        res.statusCode = 404;
    }
    return {
        snippet,
    };
};

export default Snippet;
