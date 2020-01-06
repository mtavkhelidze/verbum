import axios from "axios";
import { NextPage } from "next";
import * as React from "react";
import { Col, Row } from "reactstrap";
import Layout from "../../components/Layout";
import SentenceList from "../../components/SentenceList";
import { apiUrl } from "../../util/misc";

interface Props {
    original: Sentence;
    similar: SimilarSentence[];
}

const toNormal = (s: SimilarSentence) => ({
    id: s.id,
    body: s.body,
});

const byScore = (s1: SimilarSentence, s2: SimilarSentence) => {
    return s1.score - s2.score;
};

const SimilarSentences: NextPage<Props> = props => {
    const { original, similar } = props;
    const sim = similar.filter(s => s.id != original.id).sort(byScore);
    return (
      <Layout title={`Verbum : Sentences similar to ${original.id}`}>
          <Row className="mb-3">
              <Col xs="12" md="2"><b>Original</b></Col>
              <Col xs="12" md="10">{original.body}</Col>
          </Row>
          <Row className="mb-3">
              <Col xs="12" md="2"><b>Similar</b></Col>
              <Col xs="12" md="10">
                  <SentenceList sentences={sim} />
              </Col>
          </Row>
      </Layout>
    );
};

SimilarSentences.getInitialProps = async ({ query, res }) => {
    const id = query.id;
    return await axios
      .get<SimilarResult>(apiUrl(`/similar/${id}`))
      .then(d => d.data);
};

export default SimilarSentences;
