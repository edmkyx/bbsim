# BBSim

Online college basketball simulation game (under construction)

## How to get started

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the FastAPI backend:
   ```
   uvicorn web.main:app --reload
   ```

3. Backend API will be available at [http://localhost:8000](http://localhost:8000)

### Next Steps

- [ ] Expand player/team data model
- [ ] Improve game simulation realism
- [ ] Build out season, schedule, and recruiting features
- [ ] Implement web frontend

For more ideas, check out [jbl sim league](https://www.jblfl.com/) and [Draft Day Sports College Basketball](https://www.wolverinestudios.com/draft-day-sports-college-basketball).
