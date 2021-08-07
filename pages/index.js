import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import Header from "../components/Header";
import Nav from "../components/Nav";
import Results from "../components/Results";
import requests from "../utils/requests";
import Data from "../output/ski_slope_map.json"


export default function Home({ results }) {
  return (
    <div className="bg-gradient-to-r from-blue-100 via-blue-200 to-blue-300">
      <Head>
        <title>スノマップ</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      {/* Header */}
      <Header />

      {/* Nav */}
      <Nav />

      {/* Results */}
      <Results results={results} />
    </div>
  );
}

// 先にサーバーサイドレンダリングが走る
export async function getServerSideProps(context) {

  return {
    props: {
      results: Data,
    },
  };
}
