---
layout: default
title: Experience
permalink: /experience/
---

<p class="page-action">
  <a href="{{ '/assets/cv/Zhengyang_Wang_CV.pdf' | relative_url }}">View full CV</a>
</p>

## Preprints & Presentations

1. **[Revisiting Learning to Delegate: LLM Discovered Heuristics for Large-Scale Vehicle Routing]({{ '/papers/revisiting-learning-to-delegate/' | relative_url }})** (2026). Available on arXiv.
2. **[Incentive-Aligned Vehicle Routing with LLM Agents](https://info.informs.org/hubfs/3449182/Program_Archives/Annual/2026%20Annual%20Meeting%20Program%20Book.pdf#page=1793)** (2026). Invited presentation at the INFORMS Annual Meeting, session WB55, PDF page 1793.
3. **[Fragmented Obedient Equilibria in Routing Games](https://arxiv.org/abs/2610.39225)** (2026). Available on arXiv.
4. **[Toward Scalable Privacy in Omics Research: A Scoping Review of Privacy-Enhancing Technologies](https://doi.org/10.2139/ssrn.7164458)** (2026). Available on SSRN.

## Research Experience

<div class="entry-list">
  <article class="entry" id="llm-guided-solver-delegation">
    <div class="entry-meta">Aug 2026 - Present</div>
    <div class="entry-body">
      <h3>LLM-Guided Solver Delegation for Vehicle Routing</h3>
      <p>
        Developed a hypothesis-driven framework for automatic heuristic design
        that uses LLMs to discover which groups of routes to reoptimize in
        large-scale capacitated vehicle routing. The selected heuristic achieved
        comparable in-distribution performance while outperforming the neural
        baselines on large-scale out-of-distribution instances.
      </p>
    </div>
  </article>

  <article class="entry" id="fuel-dispatch-optimization">
    <div class="entry-meta">Mar 2026 - Present</div>
    <div class="entry-body">
      <h3>Fuel Dispatch Optimization</h3>
      <p>
        Built mixed-integer dispatch planning for AKWA Group's 700+ station
        network in Morocco. Retrospective benchmarks using the same orders
        and trucks as historical plans showed 25.5% lower average travel
        distance and 6% more delivered volume, with 97% full-order fulfillment
        versus 99.2% historically.
      </p>
      <p>
        Built a replenishment order predictor (ROC-AUC 0.92 on a chronological
        holdout) and an LLM-assisted workflow for dispatcher-requested rerouting.
      </p>
    </div>
  </article>

  <article class="entry" id="multi-mediator-congestion-games">
    <div class="entry-meta">Jan 2026 - Present</div>
    <div class="entry-body">
      <h3>Multi-Mediator Congestion Games</h3>
      <p>
        Modeled competing navigation platforms whose users can ignore private
        route recommendations. Proved existence of fragmented obedient
        equilibrium under a lower-hemicontinuity assumption and derived an
        exact flow-moment formulation under affine edge latencies and independent
        platform randomization. Using semidefinite programming for best
        responses on a Braess network, computed equilibria with total travel
        costs up to about 17% below the Wardrop benchmark and close to the
        social optimum with two equally sized populations at a looser tolerance.
      </p>
      <p><a href="https://arxiv.org/abs/2610.39225">Manuscript (arXiv)</a></p>
    </div>
  </article>

  <article class="entry">
    <div class="entry-meta">Dec 2024 - Apr 2025</div>
    <div class="entry-body">
      <h3>Dynamic Pricing under Nonlinear Demand</h3>
      <p>
        Modeled competitive online pricing as a repeated seller-buyer game and
        simulated regret, price convergence, and learning behavior under
        nonlinear demand.
      </p>
    </div>
  </article>
</div>

## Projects

<div class="entry-list">
  <article class="entry">
    <div class="entry-meta">Jan 2026 - May 2026</div>
    <div class="entry-body">
      <h3>Black Box Inverse Solver</h3>
      <p>
        Built a meta-learning workflow for uncertainty quantification in PDE
        inverse problems, mapping sparse spatiotemporal observations to
        calibrated joint confidence intervals over PDE parameters. Across PDE
        families, joint coverage was within 0.33 percentage points of the 95%
        target.
      </p>
    </div>
  </article>

  <article class="entry">
    <div class="entry-meta">Apr 2026</div>
    <div class="entry-body">
      <h3>Optimization Method Benchmarks</h3>
      <p>
        Compared gradient, Newton, quasi-Newton, and trust-region methods
        across 12 unconstrained optimization problems, finding that L-BFGS
        offered the strongest practical balance between convergence rate and
        runtime.
      </p>
    </div>
  </article>

  <article class="entry">
    <div class="entry-meta">Jun 2025 - Jan 2026</div>
    <div class="entry-body">
      <h3>Clinical NLP and Privacy-Preserving Methods</h3>
      <p>
        Built clinical NLP pipelines on MIMIC-IV notes using CUI co-occurrence
        features and contributed literature screening and data extraction for a
        scoping review on privacy-enhancing technologies in omics research.
      </p>
      <p><a href="https://doi.org/10.2139/ssrn.7164458">Manuscript (SSRN)</a></p>
    </div>
  </article>

  <article class="entry">
    <div class="entry-meta">Nov 2025</div>
    <div class="entry-body">
      <h3>Adam Revisited</h3>
      <p>
        Implemented SGD, AdaGrad, RMSProp, Adam, and AMSGrad from scratch and
        analyzed step-size behavior, second-moment dynamics, and convergence
        stability.
      </p>
    </div>
  </article>

  <article class="entry">
    <div class="entry-meta">Jan 2025 - Apr 2025</div>
    <div class="entry-body">
      <h3>Mini AlphaGo</h3>
      <p>
        Developed Go game-state preprocessing, a dual-head residual network,
        and Monte Carlo Tree Search with neural priors and value
        backpropagation.
      </p>
    </div>
  </article>

  <article class="entry">
    <div class="entry-meta">Oct 2024 - Dec 2024</div>
    <div class="entry-body">
      <h3>Random Forests and Condorcet's Jury Theorem</h3>
      <p>
        Investigated Random Forests through Condorcet's Jury Theorem and
        applied the method to early-onset diabetes prediction.
      </p>
    </div>
  </article>
</div>

## Work

<div class="entry-list">
  <article class="entry">
    <div class="entry-meta">Sep 2025 - Present</div>
    <div class="entry-body">
      <h3>Math Learning Center Tutor</h3>
      <p>
        Provide 9+ hours per week of walk-in tutoring in Calculus I–II and
        Linear Algebra. Lead weekly study groups.
      </p>
    </div>
  </article>

  <article class="entry">
    <div class="entry-meta">Jul 2025 - Aug 2025</div>
    <div class="entry-body">
      <h3>Wealth Management Summer Intern</h3>
      <p>
        Produced market briefs and presentation materials across
        frontier-industry themes, supporting client briefings and investment
        research.
      </p>
    </div>
  </article>
</div>
