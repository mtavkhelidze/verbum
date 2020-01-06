import { useRouter } from "next/router";
import * as React from "react";
import { CSSProperties } from "react";
import { Badge, Card, CardBody, Col, Row } from "reactstrap";

const style: CSSProperties = {
    cursor: "pointer",
    border: "none",
};

interface Props {
    snippet: Snippet;
}

const SnippetComponent = (props: Props) => {
    const { id, count, headline } = props.snippet;
    const router = useRouter();
    const onClick = async () => {
        await router.push("/snippet/[id]", `/snippet/${id}`);
    };
    return (
      <Card className="border-0 p-0">
          <CardBody style={style} onClick={onClick}>
              <Row>
                  <Col xs="10"><h5>{headline}</h5></Col>
                  <Col xs="2"><h3><Badge color="secondary">{count}</Badge>
                  </h3></Col>
              </Row>
          </CardBody>
      </Card>
    );
};

export default SnippetComponent;
