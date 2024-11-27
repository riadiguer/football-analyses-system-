for track_id, player in tracks['players'][0].items():
      bbox = player['bbox']
      frame = video_frames[0]

      # crop the bonding box from the frame  
      croped_image = frame[int(bbox[1]):int(bbox[3]),int(bbox[0]):int(bbox[2])]

      # save the croped image
      cv2.imwrite(f'output_video/croped_image.jpg',croped_image)
      break


# we used this code in main.py