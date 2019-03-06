#include <chrono>
using namespace std;
class Timer
{
private:
    chrono::time_point<chrono::steady_clock> m_StartTime;
public:
	void Start()
	{
	    m_StartTime = chrono::high_resolution_clock::now();
	}

	float GetDuration()
	{
	    chrono::duration<float> duration = chrono::high_resolution_clock::now() - m_StartTime;
	    return duration.count();
	}
};

int main(int argc, char const *argv[]) {
  Timer timer;
  timer.Start();
  cout << timer.GetDuration() << endl;
  return 0;
}
