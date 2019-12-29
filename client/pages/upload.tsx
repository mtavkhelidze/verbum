import { NextPage } from "next";
import { useRouter } from "next/router";
import React from "react";
import InputText from "../components/InputText";
import Layout from "../components/Layout";


const Upload: NextPage = () => {
    const router = useRouter();
    const onSave = (id: number) =>
      router.push("/snippet/[id]", `/snippet/${id}`);
    return (
      <Layout title="Verbum : Upload">
          <InputText onSave={onSave} />
      </Layout>
    );
};

export default Upload;
