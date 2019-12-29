import Link from "next/link";
import * as React from "react";
import { Col, Row } from "reactstrap";

interface Props {
    sentence: Sentence;
}

const SentenceComponent = (props: Props) => {
    return (
      <Row>
          <Col xs="10">{props.sentence.body}</Col>
          <Col xs="2">
              <Link
                href="/similar/[id]"
                as={`/similar/${props.sentence.id}`}
              >
                  <a>show similar</a>
              </Link>
          </Col>
      </Row>
    );
};

export default SentenceComponent;
