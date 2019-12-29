import * as React from "react";
import { ListGroup, ListGroupItem } from "reactstrap";
import SentenceComponent from "./SentenceComponent";

interface Props {
    sentences: Sentence[];
}

const SentenceList = (props: Props) => {
    const items = props.sentences.map(s => (
      <ListGroupItem key={s.id}>
          <SentenceComponent sentence={s} />
      </ListGroupItem>
    ));

    return (
      <ListGroup>
          {items}
      </ListGroup>
    );
};

export default SentenceList;
