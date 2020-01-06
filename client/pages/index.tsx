import axios from "axios";
import { NextPage } from "next";
import React from "react";
import Layout from "../components/Layout";
import SnippetList from "../components/SnippetList";
import { apiUrl } from "../util/misc";

interface Props {
    snippets: Snippet[];
}

const Home: NextPage<Props> = props => {
    const content = props.snippets.length
      ? <SnippetList snippets={props.snippets} />
      : <h5>No snippets yet. Use <i>Upload</i> to create some.</h5>;
    return (
      <Layout title="Verbum : Home">
          {content}
      </Layout>
    );
};

Home.getInitialProps = async () => {
    const snippets = await axios
      .get<Snippet[]>(apiUrl("/snippet"))
      .then(r => r.data);

    return { snippets };
};
export default Home;
