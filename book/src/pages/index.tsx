import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function Home() {
  return (
    <Layout title="Physical AI & Humanoid Robotics">
      <main style={{ padding: '4rem' }}>
        <h1>Physical AI & Humanoid Robotics</h1>
        <p>An AI-Native Technical Textbook</p>
        <Link to="/docs/module-1-foundations/intro">
          Start Learning →
        </Link>
      </main>
    </Layout>
  );
}