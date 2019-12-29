import axios from "axios";
import { NextPage } from "next";
import { useRouter } from "next/router";
import React from "react";
import Layout from "../components/Layout";
import SnippetList from "../components/SnippetList";

interface Props {
    snippets: Snippet[];
}

const Home: NextPage<Props> = props => {
    const router = useRouter();
    return (
      <Layout title="Verbum : Home">
          <SnippetList snippets={props.snippets} />
      </Layout>
    );
};

Home.getInitialProps = async () => {
    const snippets = await axios
      .get<Snippet[]>("http://localhost:5000/snippets")
      .then(r => r.data);

    return { snippets };
};
export default Home;
