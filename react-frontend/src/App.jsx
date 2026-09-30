import { useState, useEffect } from "react";
import {
  Activity,
  Dumbbell,
  HeartPulse,
  Apple,
  BarChart3,
  Bot,
  Flame,
  Menu,
  X,
} from "lucide-react";
import "./App.css";

function App() {
  const [bmiData, setBmiData] = useState(null);
  const [progressData, setProgressData] = useState(null);
  const [activePage, setActivePage] = useState("Dashboard");
  const [sidebarOpen, setSidebarOpen] = useState(false);

  // BMI API
  useEffect(() => {
    fetch("http://127.0.0.1:8000/fitness/bmi?weight=55&height=1.60")
      .then((response) => response.json())
      .then((data) => {
        console.log("BMI DATA:", data);
        setBmiData(data);
      })
      .catch((error) => {
        console.error("BMI API error:", error);
      });
  }, []);

  // Progress API
  useEffect(() => {
    fetch("http://127.0.0.1:8000/progress/summary")
      .then((response) => response.json())
      .then((data) => {
        console.log("PROGRESS DATA:", data);
        setProgressData(data.progress);
      })
      .catch((error) => {
        console.error("Progress API error:", error);
      });
  }, []);

  const menuItems = [
    { name: "Dashboard", icon: BarChart3 },
    { name: "AI Workout", icon: Dumbbell },
    { name: "Nutrition", icon: Apple },
    { name: "AI Trainer", icon: Activity },
    { name: "Progress", icon: HeartPulse },
    { name: "AI Assistant", icon: Bot },
  ];

  const goToPage = (page) => {
    setActivePage(page);
    setSidebarOpen(false);
  };

  return (
    <div className="app">
      {/* Mobile Header */}
      <div className="mobile-header">
        <button onClick={() => setSidebarOpen(!sidebarOpen)}>
          {sidebarOpen ? <X /> : <Menu />}
        </button>

        <h2>AI Fitness</h2>
      </div>

      {/* Sidebar */}
      <aside className={`sidebar ${sidebarOpen ? "open" : ""}`}>
        <div className="logo">
          <div className="logo-icon">
            <Dumbbell size={24} />
          </div>

          <div>
            <h2>AI Fitness</h2>
            <span>Smart Gym Assistant</span>
          </div>
        </div>

        <nav>
          {menuItems.map((item) => {
            const Icon = item.icon;

            return (
              <button
                key={item.name}
                className={activePage === item.name ? "active" : ""}
                onClick={() => goToPage(item.name)}
              >
                <Icon size={20} />
                {item.name}
              </button>
            );
          })}
        </nav>

        <div className="sidebar-bottom">
          <div className="user-card">
            <div className="avatar">S</div>

            <div>
              <strong>Spoorthi</strong>
              <small>Beginner</small>
            </div>
          </div>
        </div>
      </aside>

      {/* Main */}
      <main className="main">
        {/* Top Bar */}
        <header className="topbar">
          <div>
            <p className="welcome">Welcome back 👋</p>
            <h1>{activePage}</h1>
          </div>

          <div className="status">
            <span></span>
            System Active
          </div>
        </header>

        {/* DASHBOARD */}
        {activePage === "Dashboard" && (
          <>
            <section className="hero">
              <div>
                <p className="hero-label">YOUR FITNESS JOURNEY</p>

                <h2>
                  Train smarter.
                  <br />
                  <span>Feel stronger.</span>
                </h2>

                <p className="hero-text">
                  Your AI-powered fitness companion for workouts,
                  nutrition, progress and healthy habits.
                </p>

                <button
                  className="primary-btn"
                  onClick={() => goToPage("AI Workout")}
                >
                  Start Workout →
                </button>
              </div>

              <div className="hero-icon">
                <Dumbbell size={110} strokeWidth={1.2} />
              </div>
            </section>

            {/* Statistics */}
            <section className="stats">
              <div className="stat-card">
                <div className="stat-icon">
                  <Activity />
                </div>

                <div>
                  <span>BMI</span>

                  <h3>
                    {bmiData ? bmiData.bmi : "Loading..."}
                  </h3>

                  <small>
                    {bmiData ? bmiData.category : "Calculating..."}
                  </small>
                </div>
              </div>

              <div className="stat-card">
                <div className="stat-icon">
                  <Flame />
                </div>

                <div>
                  <span>Daily Calories</span>
                  <h3>1,499</h3>
                  <small>Recommended</small>
                </div>
              </div>

              <div className="stat-card">
                <div className="stat-icon">
                  <Dumbbell />
                </div>

                <div>
                  <span>Workouts</span>

                  <h3>
                    {progressData
                      ? progressData.total_workouts
                      : "18"}
                  </h3>

                  <small>Total sessions</small>
                </div>
              </div>

              <div className="stat-card">
                <div className="stat-icon">
                  <HeartPulse />
                </div>

                <div>
                  <span>Performance</span>

                  <h3>
                    {progressData
                      ? `${progressData.performance_score}%`
                      : "38%"}
                  </h3>

                  <small>Keep improving</small>
                </div>
              </div>
            </section>

            {/* Dashboard Grid */}
            <section className="dashboard-grid">
              {/* Today's Workout */}
              <div className="panel workout-panel">
                <div className="panel-heading">
                  <div>
                    <span className="section-label">
                      TODAY'S PLAN
                    </span>

                    <h2>Full Body Workout</h2>
                  </div>

                  <Dumbbell />
                </div>

                <div className="exercise">
                  <div>
                    <strong>Bodyweight Squats</strong>
                    <small>3 sets × 12 reps</small>
                  </div>

                  <span>12</span>
                </div>

                <div className="exercise">
                  <div>
                    <strong>Wall Push-ups</strong>
                    <small>3 sets × 10 reps</small>
                  </div>

                  <span>10</span>
                </div>

                <div className="exercise">
                  <div>
                    <strong>Glute Bridges</strong>
                    <small>3 sets × 12 reps</small>
                  </div>

                  <span>12</span>
                </div>

                <button
                  className="wide-btn"
                  onClick={() => goToPage("AI Trainer")}
                >
                  Launch AI Trainer
                </button>
              </div>

              {/* Progress */}
              <div className="panel">
                <div className="panel-heading">
                  <div>
                    <span className="section-label">
                      PROGRESS
                    </span>

                    <h2>Weekly Activity</h2>
                  </div>

                  <BarChart3 />
                </div>

                <div className="progress-circle">
                  <div>
                    <strong>
                      {progressData
                        ? `${progressData.performance_score}%`
                        : "38%"}
                    </strong>

                    <span>Performance</span>
                  </div>
                </div>

                <div className="progress-info">
                  <div>
                    <strong>
                      {progressData
                        ? progressData.total_workouts
                        : "18"}
                    </strong>

                    <span>Workouts</span>
                  </div>

                  <div>
                    <strong>
                      {progressData
                        ? progressData.total_completed_reps
                        : "64"}
                    </strong>

                    <span>Reps</span>
                  </div>

                  <div>
                    <strong>
                      {progressData
                        ? `${Math.round(
                            progressData.total_workout_duration_minutes
                          )}m`
                        : "20m"}
                    </strong>

                    <span>Duration</span>
                  </div>
                </div>
              </div>

              {/* AI Assistant */}
              <div className="panel assistant-panel">
                <div className="assistant-icon">
                  <Bot size={28} />
                </div>

                <div>
                  <span className="section-label">
                    AI FITNESS ASSISTANT
                  </span>

                  <h2>Need some motivation?</h2>

                  <p>
                    Ask me about workouts, nutrition,
                    fitness habits or your progress.
                  </p>

                  <button
                    className="secondary-btn"
                    onClick={() => goToPage("AI Assistant")}
                  >
                    Talk to AI →
                  </button>
                </div>
              </div>
            </section>
          </>
        )}

        {/* AI WORKOUT */}
        {activePage === "AI Workout" && (
          <section className="placeholder">
            <div className="placeholder-icon">
              <Dumbbell size={48} />
            </div>

            <h2>AI Workout Recommendation</h2>

            <p>
              Personalized workout plan based on your
              fitness goal and experience level.
            </p>

            <div className="workout-card">
              <h3>Weight Loss — Beginner</h3>

              <p><strong>Monday</strong></p>
              <p>• Bodyweight Squats — 3 × 12</p>
              <p>• Wall Push-ups — 3 × 10</p>
              <p>• Glute Bridges — 3 × 12</p>
              <p>• Plank — 3 × 20 sec</p>

              <p><strong>Tuesday</strong></p>
              <p>• Brisk Walking — 30 minutes</p>

              <p><strong>Wednesday</strong></p>
              <p>• Rest</p>

              <p><strong>Thursday</strong></p>
              <p>• Lunges — 3 × 10</p>
              <p>• Knee Push-ups — 3 × 10</p>
              <p>• Glute Bridges — 3 × 15</p>

              <p><strong>Friday</strong></p>
              <p>• Jumping Jacks — 3 × 20</p>
              <p>• Bodyweight Squats — 3 × 12</p>

              <p><strong>Saturday</strong></p>
              <p>• Walking / Light Jogging — 30 minutes</p>

              <p><strong>Sunday</strong></p>
              <p>• Rest</p>
            </div>

            <button
              className="primary-btn"
              onClick={() => goToPage("AI Trainer")}
            >
              Start AI Trainer →
            </button>
          </section>
        )}

        {/* NUTRITION */}
        {activePage === "Nutrition" && (
          <section className="placeholder">
            <div className="placeholder-icon">
              <Apple size={48} />
            </div>

            <h2>AI Nutrition & Calorie Coach</h2>

            <p>
              Personalized nutrition recommendations based
              on your fitness profile.
            </p>

            <div className="workout-card">
              <h3>Daily Nutrition</h3>

              <p>
                Calories:
                <strong> 1,499 kcal</strong>
              </p>

              <p>
                Goal:
                <strong> Weight Loss</strong>
              </p>

              <p>
                Diet:
                <strong> Vegetarian</strong>
              </p>

              <p>
                Protein:
                <strong> 73 g</strong>
              </p>

              <h3>Recommended Meals</h3>

              <p>• Breakfast — Oats, fruits and milk</p>
              <p>• Lunch — Rice, dal and vegetables</p>
              <p>• Snack — Fruit and nuts</p>
              <p>• Dinner — Chapati, vegetables and dal</p>

              <h3>Grocery List</h3>

              <p>• Oats</p>
              <p>• Fruits</p>
              <p>• Vegetables</p>
              <p>• Dal</p>
              <p>• Milk</p>
              <p>• Nuts</p>
            </div>

            <button
              className="primary-btn"
              onClick={() => goToPage("Dashboard")}
            >
              ← Back to Dashboard
            </button>
          </section>
        )}

        {/* AI TRAINER */}
        {activePage === "AI Trainer" && (
          <section className="placeholder">
            <div className="placeholder-icon">
              <Activity size={48} />
            </div>

            <h2>AI Exercise Trainer</h2>

            <p>
              Computer vision based exercise detection,
              repetition counting and basic form feedback.
            </p>

            <div className="workout-card">
              <h3>Supported Exercises</h3>

              <p>✓ Squats</p>
              <p>✓ Push-ups</p>
              <p>✓ Lunges</p>
              <p>✓ Glute Bridges</p>
              <p>✓ Plank</p>

              <h3>AI Features</h3>

              <p>✓ Pose detection</p>
              <p>✓ Repetition counting</p>
              <p>✓ Basic form feedback</p>
              <p>✓ Workout result tracking</p>
              <p>✓ Performance analysis</p>
            </div>

            <button
              className="primary-btn"
              onClick={() => goToPage("Dashboard")}
            >
              ← Back to Dashboard
            </button>
          </section>
        )}

        {/* PROGRESS */}
        {activePage === "Progress" && (
          <section className="placeholder">
            <div className="placeholder-icon">
              <HeartPulse size={48} />
            </div>

            <h2>Workout Progress</h2>

            <p>
              Track your workout activity and performance.
            </p>

            <div className="workout-card">
              <h3>Fitness Progress</h3>

              <p>
                Total Workouts:
                <strong>
                  {" "}
                  {progressData
                    ? progressData.total_workouts
                    : "Loading..."}
                </strong>
              </p>

              <p>
                Total Completed Reps:
                <strong>
                  {" "}
                  {progressData
                    ? progressData.total_completed_reps
                    : "Loading..."}
                </strong>
              </p>

              <p>
                Total Duration:
                <strong>
                  {" "}
                  {progressData
                    ? `${progressData.total_workout_duration_minutes} minutes`
                    : "Loading..."}
                </strong>
              </p>

              <p>
                Completed Workouts:
                <strong>
                  {" "}
                  {progressData
                    ? progressData.completed_workouts
                    : "Loading..."}
                </strong>
              </p>

              <p>
                Incomplete Workouts:
                <strong>
                  {" "}
                  {progressData
                    ? progressData.incomplete_workouts
                    : "Loading..."}
                </strong>
              </p>

              <p>
                Average Reps:
                <strong>
                  {" "}
                  {progressData
                    ? progressData.average_reps_per_workout
                    : "Loading..."}
                </strong>
              </p>

              <p>
                Performance Score:
                <strong>
                  {" "}
                  {progressData
                    ? `${progressData.performance_score}%`
                    : "Loading..."}
                </strong>
              </p>
            </div>

            <button
              className="primary-btn"
              onClick={() => goToPage("Dashboard")}
            >
              ← Back to Dashboard
            </button>
          </section>
        )}

        {/* AI ASSISTANT */}
        {activePage === "AI Assistant" && (
          <section className="placeholder">
            <div className="placeholder-icon">
              <Bot size={48} />
            </div>

            <h2>AI Fitness Assistant</h2>

            <p>
              Get intelligent assistance for workouts,
              nutrition, fitness habits and progress.
            </p>

            <div className="workout-card">
              <h3>Fitness Assistant</h3>

              <p>💬 How can I help you today?</p>

              <p>• Ask about workouts</p>
              <p>• Ask about nutrition</p>
              <p>• Ask about fitness habits</p>
              <p>• Ask about your progress</p>
              <p>• Ask for workout motivation</p>

              <h3>Example Questions</h3>

              <p>
                "What workout should I do today?"
              </p>

              <p>
                "How can I improve my fitness?"
              </p>

              <p>
                "What should I eat after a workout?"
              </p>
            </div>

            <button
              className="primary-btn"
              onClick={() => goToPage("Dashboard")}
            >
              ← Back to Dashboard
            </button>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;