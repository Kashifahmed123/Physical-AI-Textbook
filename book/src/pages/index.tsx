import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import clsx from 'clsx';

import styles from './index.module.css';

export default function Home() {
  return (
    <Layout title="Physical AI & Humanoid Robotics">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <h1 className="hero__title">Physical AI & Humanoid Robotics</h1>
          <p className="hero__subtitle">An academic and practical guide to Physical AI, Humanoid Robotics, and Embodied Intelligence</p>
          <div className="heroVisual">
            <img
              src="/img/humanoid-ai-hero.svg"
              alt="Physical AI and Humanoid Robotics"
            />
          </div>
          <div className={styles.buttons}>
            <Link
              className="button button--secondary button--lg"
              to="/docs/intro">
              Start Learning
            </Link>
          </div>
        </div>
      </header>
      <main className={styles.mainContent}>
        <div className="container">
          <section className={styles.features}>
            <div className="row">
              <div className="col col--4">
                <h2 className={styles.featureTitle}>Foundational Concepts</h2>
                <p>Explore the fundamental principles of Physical AI and embodied intelligence.</p>
              </div>
              <div className="col col--4">
                <h2 className={styles.featureTitle}>Technical Implementation</h2>
                <p>Learn practical implementation with ROS 2, NVIDIA Isaac, and modern robotics frameworks.</p>
              </div>
              <div className="col col--4">
                <h2 className={styles.featureTitle}>Advanced Applications</h2>
                <p>Discover cutting-edge applications in humanoid locomotion, manipulation, and conversational AI.</p>
              </div>
            </div>
          </section>
        </div>
      </main>
    </Layout>
  );
}