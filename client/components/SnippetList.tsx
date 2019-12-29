import * as React from "react";
import { ListGroup, ListGroupItem } from "reactstrap";
import SnippetComponent from "./SnippetComponent";

interface Props {
    snippets: Snippet[];
}

const SnippetList = (props: Props) => {
    const items = props.snippets.map(s => (
      <ListGroupItem key={s.id}>
          <SnippetComponent snippet={s} />
      </ListGroupItem>
    ));

    return (
      <ListGroup>
          {items}
      </ListGroup>
    );
};

export default SnippetList;
